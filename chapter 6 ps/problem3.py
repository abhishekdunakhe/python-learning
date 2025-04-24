spam_1 = "Make lot of money"
spam_2 = "Buy now"
spam_3 = "click this"


meaasge = input("Enter Your Meessage:")

if((spam_1 in meaasge) or (spam_2 in meaasge) or (spam_3 in meaasge) ):
    print("This messaege is spam message")

else:
    print("This is safe message for You")