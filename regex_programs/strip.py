import re

#returns a stripped string--imitating the behavior of .strip() method
def strip_string(string, strip_char=" "):
    print("\nStripping your line...")
    time.sleep(2)
    rx = re.compile(r"^[%s]+|[%s]+$" %(strip_char, strip_char))
    return rx.sub('', string) #return stripped string
    
#test strip
print(strip_string("   strip this line pls  ")) #testing whitespace default for no strip_char arg
print(strip_string("okokokstrip this line as wellkoko", strip_char="ko")) #testing different orders for same strip chars
print(strip_string("+++strip this line too++", strip_char="+")) #testing special strip_char
print(strip_string("hey strip this too", strip_char="+")) #testing no match for strip_char in string