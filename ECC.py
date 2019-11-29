import RSA
from fractions import Fraction


def verify_parameters(a, b, p):
    if (4*pow(a, 3) + 27*pow(b, 2)) % p == 0:
        return False
    else:
        return True


# params: (a, b, p)
def verify_point(x, y, params):
    if pow(y, 2) % params[2] == (pow(x, 3) + params[0]*x + params[1]) % params[2]:
        return True
    else:
        return False


def addition(P, Q, params):
    R = [0, 0]
    lamb_value = lamb(P, Q, params)

    if lamb_value is None:
        return [0, 0]

    R[0] = (pow(lamb_value, 2) - P[0] - Q[0]) % params[2]
    R[1] = (lamb_value*(P[0] - R[0]) - P[1]) % params[2]

    return R


def multiplication(P, n, params):
    if n == 1:
        return P
    elif n >= 2:
        product = addition(P, P, params)
        for i in range(n-2):
            product = addition(P, product, params)
        return product
    else:
        return []


def lamb(P, Q, params):
    if P == Q:
        fract = Fraction((3*pow(P[0], 2) + params[0]) % params[2], (2*P[1]) % params[2])
        inv = RSA.get_mod_inverse(params[2], fract.denominator)
        inv = (inv * fract.numerator) % params[2]
        return inv
    else:
        numerator = (Q[1] - P[1])
        denominator = (Q[0] - P[0])
        if denominator == 0:
            return None
        if numerator > 0:
            numerator = numerator % params[2]
        if denominator > 0:
            denominator = denominator % params[2]
        fract = Fraction(numerator, denominator)
        inv = RSA.get_mod_inverse(params[2], fract.denominator)
        inv = (inv * fract.numerator) % params[2]
        return inv
