val=input()
if val>='a' and val<='z' or val>='A' and val>='Z':
    if val=='a' or val=='e' or val=='i' or val=='o' or val=='u' or val=='A' or val=='E' or val=='I' or val=='O' or val=='U':
        print("vowel")
    else:
        print ("consonant")
else:
    print("invalid")
