import sys

with open('data.out', 'r') as handle:
    res_oficial = handle.read()

lines_oficial = res_oficial.split('\n')

res_contestant = sys.stdin.read()
lines_contestant = res_contestant.split('\n')

lines_contestant.sort()
lines_oficial.sort()
print(1 if lines_oficial == lines_contestant else 0)