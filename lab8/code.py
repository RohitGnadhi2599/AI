# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 08:34:35 2024

@author: R.N.GANDHI
"""

class ForwardChaining:
def  init (self, facts, rules): """
Initialize the Forward Chaining algorithm with facts and rules.
:param facts: Set of known facts (initial facts).
:param rules: List of rules where each rule is a tuple (premise, conclusion). """
self.facts = set(facts) self.rules = rules
self.inferred_facts = set(facts) # Set of facts derived during the process

def apply_rule(self, rule): """
Applies a rule to derive new facts from existing facts.
:param rule: A rule represented as (premise, conclusion).
:return: True if a new fact is derived, False otherwise. """
premise, conclusion = rule
premise_facts = set(premise.split(',')) # Split the premise into individual facts # Check if the premise of the rule is fully satisfied by current facts
if premise_facts.issubset(self.facts): # Ensure all premises are in facts if conclusion not in self.facts:
print(f"Inferred new fact: {conclusion}") self.facts.add(conclusion) # Add the conclusion to the set of facts return True
return False

def forward_chaining(self): """
Applies forward chaining to derive new facts until no more facts can be derived. """
new_inference = True while new_inference:
new_inference = False
# Go through all the rules and try to apply them for rule in self.rules:
if self.apply_rule(rule): new_inference = True
if new_inference:
 
print(f"Current facts: {self.facts}") print("Forward Chaining completed.")

def is_goal_reached(self, goal): """
Checks if the goal has been reached (i.e., if the goal is in the facts).
:param goal: The goal fact to check for.
:return: True if the goal is in the facts, otherwise False. """
return goal in self.facts


def main():
print("Forward Chaining System")

# Define the initial facts facts = {
"american(p)",
"weapon(q)",
"sells(p,q,r)",
"hostile(r)", "american(robert)", "enemy(a, america)"
}

# Define the rules (premise -> conclusion) rules = [
("american(p),weapon(q),sells(p,q,r),hostile(r)", "criminal(p)"), # Rule 1
("owns(a,x),missile(x)", "sells(robert,x,a)"), # Rule 2 ("missile(x)", "weapon(x)"), # Rule 3
("enemy(a,america)", "hostile(a)") # Rule 4
]

# Create an instance of ForwardChaining with the facts and rules fc = ForwardChaining(facts, rules)

# Perform forward chaining to infer new facts fc.forward_chaining()

# Define the goal (fact you want to check) goal = "criminal(robert)"
 
# Check if the goal is reached if fc.is_goal_reached(goal):
print(f"The goal '{goal}' is reached!") else:
print(f"The goal '{goal}' is reached.")

# Run the main function
if  name	== " main ": main()
