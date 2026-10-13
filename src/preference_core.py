"""Preference pairwise angular distance, translated from VBA Module3.Macro2."""
import math

def preference_distance(first, second):
    first=list(first);second=list(second)
    if len(first)!=len(second) or len(first)<2:
        raise ValueError("Both preferences must have the same length (at least two).")
    n=len(first)
    for label, values in (("Preference 1", first),("Preference 2",second)):
        for idx, v in enumerate(values,1):
            if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or int(v)!=v or not 1<=v<=n:
                raise ValueError(f"{label} row {idx}: expected an integer ranking in [1, {n}].")
    numerator=norm1=norm2=0
    for i in range(n):
        for j in range(i+1,n):
            a=(first[i]<first[j])-(first[i]>first[j])
            b=(second[i]<second[j])-(second[i]>second[j])
            numerator+=2*a*b
            norm1+=2*a*a
            norm2+=2*b*b
    if not norm1 or not norm2:
        raise ValueError("Ranking must contain at least two distinct values in each preference.")
    cosine=max(-1.,min(1.,numerator/math.sqrt(norm1*norm2)))
    return {'cosine':cosine,'distance':math.acos(cosine)/math.pi,'numerator':numerator,'norm1':norm1,'norm2':norm2}
