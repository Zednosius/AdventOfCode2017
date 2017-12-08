import re
from collections import defaultdict





var = "(\w+)"
op ="(inc|dec)"
iff = "if"
compre = "(<|>|<=|>=|==|!=)"
val = "(-?\d+)"
regex_string = "\s*".join((var,op,val,iff,var,compre,val))
regex = re.compile(regex_string)


def mod_op(env, var, op, val):
    v = env[var]
    if op == "dec":
        env[var] -= val
    elif op == "inc":
        env[var] += val
    return env


def comp_op(env, var, c_op, val):
    v = env[var]
    return eval(str(v) + c_op + val)

def parse_line(line):
    return regex.match(line).groups()
    

if __name__ == '__main__':
    data = []
    env = defaultdict(int)
    all_time_max = 0
    with open("input/day8.txt") as f:
        for line in f:
            v_var, v_op, v_val, c_var, c_op, c_val = parse_line(line)
            if comp_op(env, c_var, c_op, c_val):
                mod_op(env, v_var, v_op, int(v_val))
                all_time_max = max(all_time_max, max(env.values()))

    print("Largest value is:", max(env.values()))
    print("Largest value during execution is:", all_time_max)
