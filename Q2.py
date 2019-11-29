import ECC
import RSA

# Parameters
p = 10786642689987499259320646918494682491945365327464381078140815274881953229927397065877879182870434114159719663774278868507020738797553682933472831217132649
a = -1
b = 1
params = (a, b, p)
temp_p = 23
temp_a = 1
temp_b = 1
temp_params = (temp_a, temp_b, temp_p)
G = [3, 5]

print(ECC.verify_parameters(temp_a, temp_b, temp_p))

# print(ECC.lamb([3, 10], [9, 7], temp_params))

# print(RSA.get_mod_inverse(23, 2))
print(ECC.addition([3, 10], [9, 7], temp_params))
print(ECC.multiplication([3, 10], 28, temp_params))


