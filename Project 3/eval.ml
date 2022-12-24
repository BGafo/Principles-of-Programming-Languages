open Ast

exception TypeError
exception UndefinedVar
exception DivByZeroError

(* Remove shadowed bindings *)
let prune_env (env : environment) : environment =
  let binds = List.sort_uniq compare (List.map (fun (id, _) -> id) env) in
  List.map (fun e -> (e, List.assoc e env)) binds

(* Env print function to stdout *)
let print_env_std (env : environment): unit =
  List.fold_left (fun _ (var, value) ->
      match value with
        | Int_Val i -> Printf.printf "- %s => %s\n" var (string_of_int i)
        | Bool_Val b -> Printf.printf "- %s => %s\n" var (string_of_bool b)
        | Closure _ -> ()) () (prune_env env)

(* Env print function to string *)
let print_env_str (env : environment): string =
  List.fold_left (fun acc (var, value) ->
      match value with
        | Int_Val i -> acc ^ (Printf.sprintf "- %s => %s\n" var (string_of_int i))
        | Bool_Val b -> acc ^ (Printf.sprintf "- %s => %s\n" var (string_of_bool b))
        | Closure _ -> acc
      ) "" (prune_env env)


(***********************)
(****** Your Code ******)
(***********************)

(* evaluate an arithmetic expression in an environment *)
let rec var_search_env vari = function
| [] -> raise UndefinedVar
| (x,y)::t -> if x = vari then y else var_search_env vari t

let rec eval_expr (e : exp) (env : environment) : value =
    match e with
    | Var variable -> var_search_env variable env
    | Number integer -> Int_Val integer
    | Plus (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | Int_Val x, Int_Val y -> Int_Val (x+y)
        | _ -> raise TypeError)
    | Minus (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | Int_Val x, Int_Val y -> Int_Val (x-y)
        | _ -> raise TypeError)
    | Times (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | Int_Val x, Int_Val y -> Int_Val (x*y)
        | _ -> raise TypeError)
    | Div (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | Int_Val x, Int_Val y -> if y = 0 then raise DivByZeroError else Int_Val (x/y)
        | _ -> raise TypeError)
    | Mod (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | Int_Val x, Int_Val y -> if y = 0 then raise DivByZeroError else Int_Val (x mod y)
        | _ -> raise TypeError)
    | Eq (e1,e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Int_Val x, Int_Val y) -> Bool_Val (x = y)
        | _ -> raise TypeError)
    | Leq (e1,e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Int_Val x, Int_Val y) -> Bool_Val (x <= y)
        | _ -> raise TypeError)
    | Lt (e1,e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Int_Val x, Int_Val y) -> Bool_Val (x < y)
        | _ -> raise TypeError)
    | Not e ->
        (match eval_expr e env with
        | (Bool_Val x) -> Bool_Val (not x)
        | _ -> raise TypeError)
    | And (e1,e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Bool_Val x, Bool_Val y) -> Bool_Val (x && y)
        | _ -> raise TypeError)
    | Or (e1,e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Bool_Val x, Bool_Val y) -> Bool_Val (x || y)
        | _ -> raise TypeError)
    | True -> Bool_Val true
    | False -> Bool_Val false
    | Fun (x,e) -> Closure (env, x, e)
    | App (e1, e2) ->
        (match eval_expr e1 env, eval_expr e2 env with
        | (Closure (env', x, e'), value_of_e2) ->
            eval_expr e' ((x,value_of_e2)::env')
        | _ -> raise TypeError)
 

(* evaluate a command in an environment *)
let rec assign_new_values new_variable assigned_value = function
	| [] -> raise UndefinedVar
	| (curr_var, assigned_body)::t -> if curr_var = new_variable then
		match assigned_value, assigned_body with
		| Bool_Val bool1, Bool_Val bool2 -> (curr_var, assigned_value)::t
		| Int_Val int1, Int_Val int2 -> (curr_var, assigned_value)::t
        | closure_val -> (curr_var, assigned_value)::t
		else (curr_var, assigned_body)::assign_new_values new_variable assigned_value t

let rec dec_vari new_var dat_type = function
    | [] -> [(new_var, dat_type)]
	| (a, b)::t -> if new_var = a then (new_var, dat_type)::t
	else (a,b)::(dec_vari new_var dat_type t)

let rec eval_command (c : com) (env : environment) : environment =
    match c with
	| Skip -> env
	| Comp (former, latter) -> eval_command latter (eval_command former env)
	| Declare (type_of_input, string) -> 
		(match type_of_input with
		| Int_Type -> dec_vari string (Int_Val 0) env
		| Bool_Type -> dec_vari string (Bool_Val false) env
        | Lambda_Type -> dec_vari string (Closure (env, "x", Var "x")) env)
	| Assg (str, expres) -> assign_new_values str (eval_expr expres env) env
	| Cond (guard_expression, if_body, else_body) ->
		(match (eval_expr guard_expression env) with
		| Bool_Val bool -> if bool then eval_command if_body env else eval_command else_body env
		| _ -> raise TypeError)
	| While (guard_expression, body_command) -> 
		(match (eval_expr guard_expression env) with
		| Bool_Val bool -> if bool then (eval_command c (eval_command body_command env)) else env
		| _ -> raise TypeError)
	| For (guard_expression, body_command) ->
		(match (eval_expr guard_expression env) with
		| Int_Val n -> if n > 0 then eval_command (For (Number (n-1), body_command)) (eval_command body_command env)
		else env
		| _ -> raise TypeError)
 
