def check_length(password):
    return len(password) >= 8

def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False

def check_upper(password):
    for char in password:
        if char.isupper():
            return True
    return False

def check_lower(password):
    for char in password:
        if char.islower():
            return True
    return False

def check_special(password):
    for char in password:
        if not char.isalnum():
            return True
    return False

def validate_password(password):
    errors = []
    
    if not check_length(password):
        errors.append("недостатня довжина (менше 8 символів)")
    if not check_digit(password):
        errors.append("немає цифр")
    if not check_upper(password):
        errors.append("немає великої літери")
    if not check_lower(password):
        errors.append("немає малої літери")
    if not check_special(password):
        errors.append("немає спеціального символу")
        
    if len(errors) == 0:
        return True, []
    else:
        return False, errors

def main():
    password = input("Введіть пароль: ")
    is_valid, errors = validate_password(password)
    
    if is_valid:
        print("Пароль надійний.")
    else:
        print("Пароль не відповідає вимогам.")
        print("Не виконано:", ", ".join(errors))

if __name__ == "__main__":
    main()
```[cite: 26, 27]
