name = input("გთხოვთ შეიყვანოთ თქვენი სახელი:")


surname = input("გთოვთ შეიყვანოთ თქვენი გვარი:")

print(" ")

print("გამარჯობა! მოგესალმებათ GOA ბანკი" + " " + name + " " + surname)

print(" ")

print("ქვემოთ მოცემული ვარიანტებიდან რომლის არჩვა გსურთ?")

print(" ")

print("1)ბარათზე თანხის შეტანა") 

print(" ")

print("2)ბარათიდან თანხის გამოტანა")

print(" ")

print("3)მობილურზე თანხის შეტანა")

print(" ")

print("4)სესხის დაფარვა")    

print(" ")

print("5)სესხის აღება")

print(" ")

print("6)კომუნალურები")

print(" ")



archevani = input("რომლის არჩევა გსურთ?  არჩევანი დააფიქსირეთ ნომრით:")



if archevani == "1":
    print(" ")
    print("თვენი არჩევანი არის ბარათზე თანხის შეტანა ")
    print(" ")
    print("რომელი ბარათს შევსება გსურთ?:")
    print(" ")
    print("1)საქართველოს ბანკი")
    print("2)თიბისი ბანკი")
    print("3)გოა ბანკი")
    print(" ")
    banki = input("რომელი არჩევა გსურთ?:")
    print(" ")
    if banki == "1":
        print(" ")
        print("თქვენ აირჩეთ საქართველოს ბანკი")
        print(" ")
        print("როგორ გსურთ ბარათის შევსება")
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ")
        barati = input("რომლის არჩვა გსურთ?:")
        if barati == "1":
            print(" ")
            print("თქვენ აირჩიეთ ანგარიშის ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშის ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "2":
            print(" ")
            print("თქვენ აირჩეთ პირადი ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "3":
            print(" ")
            print("თქვენ აირჩიეთ მობილური ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif banki == "2":
        print(" ")
        print("თქვენ აირჩიეთ თიბისი ბანკი")
        print(" ")
        print("როგორ გსურთ ბარათის შევსება")
        print(" ")
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ")
        barati = input("რომლის არჩევა გსურთ?:")
        if barati == "1":
            print(" ")
            print("თქვენ აირჩეთ ანგარიშის ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშის ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "2":
            print(" ")
            print("თქვენ აირჩეთ პირადი ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "3":
            print(" ")
            print("თქვენ აირჩიეთ მობილური ნომრით ბარათის შევსება")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif banki == "3":
        print(" ")
        print("თქვენ აირჩიეთ გოა ბანკი")
        print(" ")
        print("როგორ გსურთ ბარათის შევსება")
        print(" ")
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ")
        barati = input("რომლის არჩევა გსურთ?:")
        if barati == "1":
            print(" ")
            print("თქვენ აირჩიეთ ანგარიშის ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშოს ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "2":
            print(" ")
            print("თქვენ აირჩიეთ პირადი ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati == "3":
            print(" ")
            print("თქვენ აირჩიეთ მობილური ნომრით ბარათის შევსება")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი")
            print(" ")
            tanxa = input("რა თანხის შეტანა გსურთ?:")
            print(" ")
            print("თქვენი ანგარიში შეივსო" + " " + tanxa + " " + "ლარით")
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    
#------------


elif archevani == "2":
    print("თქვენი არჩევანი არის ბარათიდან თანხის გამოტანა")
    print(" ")
    print("რომელი ბარათიდან გსურთ თანხის გამოტანა:")
    print(" ")
    print("1)საქართლოს ბანკი")
    print("2)თიბისი ბანკი")
    print("3)გოა ბანკი")
    print(" ")
    banki = input("რომელი ბარათიდან გსურთ თნხის გამოტანა?:")
    if banki == "1":
        print(" ")
        print("თქვენ აირჩიეთ საქართველის ბანკი")
        print(" ")
        print("როგორ გსურთ ბარათიდან თანხის გამოტანა?")
        print(" ")
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ")
        barati3 = input("რომლის არეჩვა გსურთ?:")
        if barati3 == "1":
            print(" ")
            print("თქვენ აირჩეთ ანგარიშის ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშის ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "2":
            print(" ") 
            print("თქვენ აირჩიეთ პირადი ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "3":
            print(" ") 
            print("თქვენ აირჩეთ მობილური ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ")
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif banki == "2":
        print(" ") 
        print("თქვენ აირჩიეთ თიბისი ბანკი")
        print(" ") 
        print("როგორ გსურთ ბარათიდან თანხის გამოტანა?")
        print(" ") 
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ") 
        barati3 = input("რომლის არჩვა გსურთ?:")
        if barati3 == "1":
            print(" ") 
            print("თქვენ აირჩიეთ ანგარიშის ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშის ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩმოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "2":
            print(" ") 
            print("თქვენ აირჩიეთ პირადი ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "3":
            print(" ") 
            print("თქვენ აირჩეთ მობილური ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif banki == "3":
        print(" ") 
        print("თქვენ აირჩიეთ გოა ბანკი")
        print(" ") 
        print("როგორ გსურთ ბარათიდან თანხის გამოტანა?")
        print("1)ანგარიშის ნომრით")
        print("2)პირადი ნომრით")
        print("3)მობილური ნომრით")
        print(" ") 
        barati3 = input("რომლის არჩევა გსურთ?:")
        if barati3 == "1":
            print(" ") 
            print("თქვენ აირჩიეთ ანგარიშის ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი ანგარიშის ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "2":
            print(" ") 
            print("თქვენ აირჩიეთ პირადი ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი პირადი ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიშიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif barati3 == "3":
            print(" ") 
            print("თქვენ აირჩიეთ მობილური ნომრით ბარათიდან თანხის გამოტანა")
            print(" ")
            input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი")
            print(" ") 
            tanxa6 = input("რა თანხის გამოტანა გსურთ?:")
            print(" ") 
            print("თქვენ ანგარიდან ჩამოგეჭრათ" + " " + tanxa6 + " " + "ლარი")
            print(" ") 
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

#---------------------
        
        
elif archevani == "3":
    print(" ") 
    print("მობილურზე თანხის შეტანა")
    print(" ") 
    print("რომელ ქსელზე გსურთ თანხის შტანა?:")
    print(" ") 
    print("1)მაგთი")
    print("2)ბილაინი")
    print("3)ჯეოსელი")
    print(" ")
    qseli = input("რომლის არჩვა გსურთ?:")
    print(" ")
    print("1)საკუთრი ანგარიში")
    print("2)სხვისი ანგარიში")
    angarishi = input("სად გსურთ თანხის შეტანა")
    if angarishi == "1":
        print("თქვენ აირჩიეთ საკუთარ ანგარიშზე თანხის")
        print(" ")
        if qseli == "1":
            print("თქვენ აირჩეთ მაგთი")
            print(" ") 
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif qseli == "2":
            print(" ") 
            print("თქვენ აირჩიეთ ბილაინი")
            print(" ")
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შეივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif qseli == "3":
            print(" ") 
            print("თქვენ აირჩიეთ ჯეოსელი")
            print(" ")
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შეივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif angarishi == "2":
        print("თვენ აირჩიეთ სხვის ანგარიშზე თანხის შეტანა")
        print(" ")
        if qseli == "1":
            print(" ") 
            print("თქვენ აირჩეთ მაგთი")
            print(" ") 
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif qseli == "2":
            print(" ") 
            print("თქვენ აირჩიეთ ბილაინი")
            print(" ")
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შეივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif qseli == "3":
            print(" ") 
            print("თქვენ აირჩიეთ ჯეოსელი")
            print(" ")
            num = input("გთხოვთ შეიყვანოთ თქვენი მობილური ნომერი:")
            print(" ") 
            tanxa3 = input("რა რაოდენობის თანხის შეტანა გსურთ?:")
            print(" ") 
            print("თქვენი ბალანსი შეივსო" + " " + tanxa3 + " " + "ლარით")
            print(" ") 
            print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")


#--------------------------------------


elif archevani == "4":
    print(" ")
    print("სესხის დაფარვა")
    print(" ")
    print("თქვენს სახელზეა 3 სესხი")
    print(" ") 
    print("რა სახის სესხის დაფარვა გსურთ?:")
    print(" ")
    print("1)სამომხმარებლო სესხი")
    print("2)ავტო სესხი")
    print("3)სტუდენტური სესხი")
    print(" ")
    sesxi = input("რომლის არჩვა გსურთ?:")
    if sesxi == "1":
        print(" ")
        print("თქვენ აირჩიეთ სამომხმარებლო სესხი")
        print(" ")
        tanxa4 = input("რა რაოდენობით გსურთ სესხის დაფარვა? სულ გადასახდელია:2540:")
        print(" ")
        print("თქვენ სესხი დაფარეთ" + " " + tanxa4 + " " + "ლარით")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif sesxi == "2":
        print(" ")
        print("თქვენ აირჩიეთ ავტო სესხი")
        print(" ")
        tanxa4 = input("რა რაოდენობით გსურთ სესხის დაფარვა?: სულ გადასახდელია 1500:")
        print(" ")
        print("თქვენ სესხი დაფარეთ" + " " + tanxa4 + " " + "ლარით")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        print(" ")
    elif sesxi == "3":
        print("თქვენ აირჩიეთ სტუდენტური სესხი")
        print(" ")
        tanxa4 = input("რა რაოდენობით გსურთ სესხის დაფარვა? სულ გადასახდელია 970:")
        print(" ")
        print("თქვენ სესხი დაფარეთ" + " " + tanxa4 + " " + "ლარით")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

#---------------------------------


elif archevani == "5":
    print(" ")
    print("სესხის აღება")
    print(" ")
    print("თქვენს სახელზეა 3 სესხი")
    print(" ")
    print("რა სახის სესხის აღება გსურთ?:")
    print(" ")
    print("1)სამომხმარებლო სესხი")
    print("2)ავტო სესხი")
    print("3)სტუდენტური სესხი")
    print(" ")
    sesxi2 = input("რომლის არჩვა გსურთ?:")
    if sesxi2 == "1":
        print(" ")
        print("თქვენ აირჩიეთ სამომხმარებლო სესხი")
        print(" ")
        tanxa5 = input("რა რაოდენობის სესხის აღება გსურთ? სულ ხელმისაწვდომია:2250:")
        print(" ")
        print("თქვენ დაგერიცხათ" + " " + tanxa5 + " " + "ლარი")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
    elif sesxi2 == "2":
        print(" ")
        print("თქვენ აირჩეით ავტო სესხი")
        print(" ")
        tanxa5 = input("რა რაოდენობის სესხის აღება გსურთ?: სულ ხელმისაწვდომია 1400:")
        print(" ")
        print("თქვენ დაგერიცხათ" + " " + tanxa5 + " " + "ლარი")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        print(" ")
    elif sesxi2 == "3":
        print("თქვენ აირჩიეთ სტუდენტური სესხი")
        print(" ")
        tanxa5 = input("რა რაოდენობის სესხის აღება გსურთ? სულ ხელმისაწვდომია 3470:")
        print(" ")
        print("თქვენ დაგერიცხათ" + " " + tanxa5 + " " + "ლარი")
        print(" ")
        print("გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

    #---------------------------------------------



elif archevani == "6":
    print("კომუნალურები")
    print(" ")
    print("1)გაზი")
    print("2)წყალი")
    print("3)ელექტრო ენერგია")
    print("4)ინტერნეტი")
    print(" ")
    komunalurebi = input("რომელი კომუნალურის გადახდა გსურთ?:")
    print(" ")
    if komunalurebi == "1":
        print("თქვენ აირჩიეთ გაზი")
        print(" ")
        gazi = input("გსურთ რომ ახლა გადაიხადოთ გაზი? გადასახდელია 20.50თ:")
        print(" ")
        if gazi == "კი":
            print(" ")
            print("თქვენ ბარათიდან ჩამოგეჭრათ 20.50ლ")
            print(" ")
            qvitari = input("გნებავთ ქვითრი?:")
            print(" ")
            if qvitari == "კი":
                print("ინებეთ ქვითარი")
                print(" ")
            elif qvitari == "არა":
                print(" ")
                print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
                print(" ")
        elif gazi == "არა":
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
            print(" ")
    elif komunalurebi == "2":
        wyali = input("გსურთ რომ ახლა გადაიხადოთ წყალი? გადასახდელია - 54ლ") 
        print(" ")
        if wyali == "კი":
            print(" ")
            print("თქვენ ბარათიდან ჩამოგეჭრათ 54ლ")
            print(" ")
            qvitari = input("გნებავთ ქვითრი?:")
            if qvitari == "კი":
                print(" ")
                print("ინებეთ ქვითარი")
            elif qvitari == "არა":
                print(" ")
                print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
                print(" ")
        elif wyali == "არა":
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
            print(" ")
    elif komunalurebi == "3":
        print(" ")
        eleqtro_energia = input("გსურთ რომ ახლა გადაიხადოთ ელექტრო ენერგია? გადასახდელია 112.50ლ:")
        print(" ")
        if eleqtro_energia == "კი":
            print("თქვენ ბარათიდან ჩამოგეჭრათ 112.5ლ")
            print(" ")
            qvitari = input("გნებავთ ქვითრი?:")
            print(" ")
            if qvitari == "კი":
                print(" ")
                print("ინებეთ ქვითარი")
            elif qvitari == "არა":
                print(" ")
                print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
        elif eleqtro_energia == "არა":
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
            print(" ")
    elif komunalurebi == "4":
        print(" ")
        interneti = input("გსურთ რომ ახლა გადაიხადოთ ელექტრო ენერგია? გადასახდელია 46.60ლ:")
        print(" ")
        if interneti == "კი":
            print(" ")
            print("თქვენი ბარათიდან ჩამოგეჭრათ 46.60ლ") 
            print(" ")
            qvitari = input("გნებავთ ქვითრი?:")
            print(" ")
            if qvitari == "კი":
                print(" ")
                print("ინებეთ ქვითარი")
                print(" ")
            elif qvitari == "არა":
                print(" ")
                print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")
                print(" ")
        elif interneti == "არა":
            print(" ")
            print("ოპერაცია დასრულებულია,გმადლობთ რომ სარგებლობთ GOA-ს ბანკომატით")

 