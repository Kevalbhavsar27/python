import re
def is_strong_password(password):
    regex_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    if re.fullmatch(regex_pattern, password):
        return True
    else:
        return False
print(f"'StrongP@ss1' is strong: {is_strong_password('StrongP@ss1')}")
print(f"'weakpassword' is strong: {is_strong_password('weakpassword')}")
print(f"'Weak123!' is strong: {is_strong_password('Weak123!')}")
print(f"'Weak123' is strong: {is_strong_password('Weak123')}")
