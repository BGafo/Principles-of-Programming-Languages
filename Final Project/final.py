from prolog_structures import Rule, RuleBody, Term, Function, Variable, Atom, Number
from typing import List
from functools import reduce

import sys
import random

class Not_unifiable(Exception):
    pass

'''
Please read prolog_structures.py for data structures
that represent Prolog terms, rules, and goals.
'''
class Interpreter:
	def __init__(self):
		pass

	'''
	Example
	occurs_check (v, t) where v is of type Variable, t is of type Term.
	occurs_check (v, t) returns true if the Prolog Variable v occurs in t.
	Please see the lecture note Control in Prolog to revisit the concept of
	occurs-check.
	'''
	def occurs_check (self, v : Variable, t : Term) -> bool:
		if isinstance(t, Variable):
			return v == t
		elif isinstance(t, Function):
			for t in t.terms:
				if self.occurs_check(v, t):
					return True
			return False
		return False


	'''
	Problem 1
	variables_of_term (t) where t is of type Term.
	variables_of_clause (c) where c is of type Rule.

	The function should return the Variables contained in a term or a rule
	using Python set.

	The result must be saved in a Python set. The type of each element (a Prolog Variable)
	in the set is Variable.
	'''
	def variables_of_term (self, t : Term) -> set :
		terms = set()
		for i in t.terms:
			if isinstance(i, Variable):
				terms.add(i)
		return terms

	def variables_of_clause (self, c : Rule) -> set :
		rules = set()
		for i in c.head.terms:
			if isinstance(i, Variable):
				rules.add(i)
		return rules


	'''
	Problem 2
	substitute_in_term (s, t) where s is of type dictionary and t is of type Term
	substitute_in_clause (s, t) where s is of type dictionary and c is of type Rule,

	The value of type dict should be a Python dictionary whose keys are of type Variable
	and values are of type Term. It is a map from variables to terms.

	The function should return t_ obtained by applying substitution s to t.

	Please use Python dictionary to represent a subsititution map.
	'''
	def substitute_in_term (self, s : dict, t : Term) -> Term:
		new_terms = []
		if isinstance(t, Function):
			for term in t.terms:
				new_terms.append(s.get(term,term))
			return Function(t.relation, new_terms)

	def substitute_in_clause (self, s : dict, c : Rule) -> Rule:
		new_rules = []
		if isinstance(c, Rule):
			for rule in c.head.terms:
				new_rules.append(s.get(rule,rule))
			return Rule(Function(c.head.relation, new_rules), c.body)


	'''
	Problem 3
	unify (t1, t2) where t1 is of type term and t2 is of type Term.
	The function should return a substitution map of type dict,
	which is a unifier of the given terms. You may find the pseudocode
	of unify in the lecture note Control in Prolog useful.

	The function should raise the exception raise Not_unfifiable (),
	if the given terms are not unifiable.

	Please use Python dictionary to represent a subsititution map.
	'''


	def unify (self, t1: Term, t2: Term) -> dict:
		s = dict({})
		if isinstance(t1, Variable) and not(self.occurs_check(t1, t2)):
			if t1 != t2:
				if not isinstance(t2, Variable):
					s[t1] = t2
				else:
					s[t2] = t1
			return s
		elif isinstance(t2, Variable) and not(self.occurs_check(t2, t1)):
			if t1 != t2:
				if not isinstance(t1, Variable):
					s[t2] = t1
				else:
					s[t1] = t2
			return s
		elif t1 == t2 and (isinstance(t1, Variable) and isinstance(t2, Variable) or isinstance(t1, Number) and isinstance(t2, Number) or isinstance(t1, Atom) and isinstance(t2, Atom)):
			return s
		elif isinstance(t1, Function) and isinstance(t2, Function):
			for i in range(len(t1.terms)):
				for j in range(len(t2.terms)):
					s.update(self.unify( t1.terms[i], t2.terms[j] ))
		else:
			raise Not_unifiable
		
		for k in s:
			for l in s:
				if k == s[l]:
					s[l] = s[k] 
		return s



		

	fresh_counter = 0
	def fresh(self) -> Variable:
		self.fresh_counter += 1
		return Variable("_G" + str(self.fresh_counter))
	def freshen(self, c: Rule) -> Rule:
		c_vars = self.variables_of_clause(c)
		theta = {}
		for c_var in c_vars:
			theta[c_var] = self.fresh()

		return self.substitute_in_clause(theta, c)


	'''
	Problem 4
	Following the Abstract interpreter pseudocode in the lecture note Control in Prolog to implement
	a nondeterministic Prolog interpreter.

	nondet_query (program, goal) where
		the first argument is a program which is a list of Rules.
		the second argument is a goal which is a list of Terms.

	The function returns a list of Terms (results), which is an instance of the original goal and is
	a logical consequence of the program. See the tests cases (in src/main.py) as examples.
	'''
	def nondet_query (self, program : List[Rule], pgoal : List[Term]) -> List[Term]:
		resolvent = pgoal
		terms = []
		while resolvent:
			# temp_goal = pgoal[random.randint(0,len(resolvent))]
			temp_goal = pgoal[0]
			
			if program[0].head.relation == temp_goal.relation and len(program[0].head.terms) == len(temp_goal.terms):
				if program[0].head.terms[0] == temp_goal.terms[0] and program[0].head.terms[1] == temp_goal.terms[1]:
					return pgoal
				elif isinstance(temp_goal.terms[0], Variable) and program[0].head.terms[1] == temp_goal.terms[1]:
					terms.append(program[0].head)
					return terms
				elif isinstance(temp_goal.terms[1], Variable) and program[0].head.terms[0] == temp_goal.terms[0]:
					terms.append(program[0].head)
					return terms
				elif isinstance(temp_goal.terms[0], Variable) and isinstance(temp_goal.terms[1], Variable):
					terms.append(program[0].head)
					return terms			
			resolvent.pop()
			# s.freshen(program)
		return pgoal


	
