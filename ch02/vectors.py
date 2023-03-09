from math import sqrt, sin, cos, atan2

def v_add(v1,v2):
    return (v1[0] + v2[0], v1[1] + v2[1])

def v_subtract(v1,v2):
    return (v1[0] - v2[0], v1[1] - v2[1])

def v_length(v):
    return sqrt(v[0]**2 + v[1]**2)

def v_distance(v1,v2):
    return v_length(v_subtract(v1,v2))
