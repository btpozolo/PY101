def xor(arg_1, arg_2):
    if (arg_1 and arg_2) or ((not arg_1) and (not arg_2)):
        return False
    else:
        return True
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)