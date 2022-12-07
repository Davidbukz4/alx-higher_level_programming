#!/usr/bin/python3

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

new_set = set()
new_set = cs_courses.union(art_courses)
new_set = new_set.intersection(cs_courses)
print(new_set)
