import re, time

#to return whether a pass is strong or not based on four password criteria
def check_password(psw):
    print("\nChecking your password...")
    time.sleep(2)
    #criteria regex
    requirements = {
        re.compile(r'.{8,}'): "8 character minimum",
        re.compile(r'[a-z]+'): "1 lowercase character minimum",
        re.compile(r'[A-Z]+'): "1 uppercase character minimum",
        re.compile(r'\d+'): "1 digit minimum"
    }
    missing_reqs = False
    for rx, req in requirements.items():
        if rx.search(psw) == None:
            print(f"Your password does not meet the {req} requirement")
            missing_reqs = True
    if not missing_reqs:
        print("Great Job! You've got a strong password")
    time.sleep(1.5)

#to return a stripped string--imitating the behavior of .strip() method
def strip_string(string, strip_char=" "):
    print("\nStripping your line...")
    time.sleep(2)
    rx = re.compile(r"^[%s]+|[%s]+$" %(strip_char, strip_char))
    return rx.sub('', string) #return stripped string

#test password
check_password("--")
check_password("StrongPassword123")

#test strip
print(strip_string("   strip this line pls  ")) #testing whitespace default for no strip_char arg
print(strip_string("okokokstrip this line as wellkoko", strip_char="ko")) #testing different orders for same strip chars
print(strip_string("+++strip this line too++", strip_char="+")) #testing special strip_char
print(strip_string("hey strip this too", strip_char="+")) #testing no match for strip_char in string