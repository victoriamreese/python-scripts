#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:17:17 2019

@author: vicky
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 18:53:50 2019

@author: vicky
"""

class Attendee():
    def __init__(self, score, identifier):
        self.score = score
        self.identifier = identifier
    def __repr__(self):
        return '{1} - {0}'.format(self.score, self.identifier)
    
import string
import random
def generate_attendee():
    score = random.randint(0,101)
    name = "".join([random.choice(string.ascii_letters) for x in range(8)])
    return Attendee(score, name)


def generate_meetup(attendance_size):
    meet_list = [generate_attendee() for x in range (attendance_size)]
    return meet_list
    
def team_assignments(meet_list):
    sorted_attendees = sorted(meet_list, key = lambda x: x.score)
    teams = []
    # what if they don't divide into 4???
    while len(sorted_attendees)>=4:
        mem1 = sorted_attendees.pop()
        mem2 = sorted_attendees.pop(0)
        mem3 = sorted_attendees.pop()
        mem4 = sorted_attendees.pop(0)
        teams.append([mem1, mem2, mem3, mem4])
    if len(sorted_attendees)==3:
        teams.append(sorted_attendees)
    else:    
        while len(sorted_attendees)>0:
            teams=sorted(teams, key = team_score)
            teams[0].append(sorted_attendees.pop())
    return teams

def add_attendees(meet_list,new_attendees):
    new_members = generate_meetup(new_attendees)
    new_meet_list = meet_list.append(new_members)
    return team_assignments(new_meet_list)
    
    
def team_score(team):
   return sum(x.score for x in team)


add_attendees(generate_meetup(25),5)

#tests
print('test 1')
mike = Attendee(7, 'mike')
assert 'mike - 7' == repr(mike)
random_attendee = generate_attendee()
print (random_attendee)
print()
print('test 2')
meet_list = generate_meetup(20) 
print(meet_list)
print(meet_list[0])
print([team_score(team) for team in meet_list])
print('test 3')
meet_list = generate_meetup(21) 
print(meet_list)
print(meet_list[0])
print([team_score(team) for team in meet_list])
print([len(team) for team in meet_list])


print('success')

print(add_attendees())
    