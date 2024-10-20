from fractions import Fraction

def is_root(s, w, dgr_a, *params):
    s = Fraction(s)
    w = Fraction(w)
    coeffs_a = list(map(Fraction, params[0: dgr_a + 1]))
    dgr_b = params[dgr_a + 1]
    coeffs_b = list(map(Fraction, params[dgr_a + 2:]))
    nominator = sum(coeff * (s ** (dgr_a - i)) for i, coeff in enumerate(coeffs_a))
    denominator = sum(coeff * (s ** (dgr_b - i)) for i, coeff in enumerate(coeffs_b))
    if denominator != 0 and Fraction(nominator, denominator) == w:
        return True
    return False

inp = eval(input())
print(is_root(*inp))
