import re, time

#to return whether a pass is strong or not based on four password criteria
def check_password(psw):
    print("\nChecking your password...")
    #time.sleep(2) --can uncomment for demo
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
    #time.sleep(1) --can uncomment for demo

#test password
check_password("--")
check_password("StrongPassword123")
