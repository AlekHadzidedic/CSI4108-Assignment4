import math


def encrypt(message, e, n):
    ciphertext = pow(message, e, n)
    return ciphertext


def decrypt_no_crt(ciphertext, d, n):
    message = pow(ciphertext, d, n)
    return message


def decrypt_crt(ciphertext, d, n, p, q, vpe, vqe):
    vp = pow(ciphertext, vpe, p)
    vq = pow(ciphertext, vqe, q)
    xp = q * (get_mod_inverse(p, q) % p)
    xq = p * (get_mod_inverse(q, p) % q)
    message = (vp*xp + vq*xq) % n
    return message


def extended_euclidean_algorithm(a, b):
    x = [1, 0]
    y = [0, 1]
    r = a % b
    q = math.floor(a/b)
    x.append(x[0] - q * x[1])
    y.append(y[0] - q * y[1])

    while r != 0:
        a = b
        b = r
        r = a % b
        q = math.floor(a/b)
        x[0] = x[1]
        x[1] = x[2]
        x[2] = x[0] - q * x[1]
        y[0] = y[1]
        y[1] = y[2]
        y[2] = y[0] - q * y[1]

    return b, x[1], y[1]


def get_mod_inverse(a, b):
    d, x, y = extended_euclidean_algorithm(a, b)
    return y







