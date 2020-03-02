is_male = False
is_tall = True

if is_male and is_tall:
    print("you are a male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("you are not male but are tall")
else:
    print("you are not a male ")
