program = True # متغير لبرنامج تسجيل الدخول
while program == True: # تكرار العملية 
 username = input("enter your user: ") #متغير لادخال اسم المستخدم
 password = input("enter your password: ") #متغير لادخال كلمة المرور

 if username == "exilelrq80" and password == "053449":  #شرط أن يكون اسم المستخدم وكلمة المرور كالتالي 
    break # في حال السطر السابق كان صحيح سنخرج من الحلقة التكرارية
 if username != "exilelrq80" or password != "053449" : #شرط أن لا يكون اسم المستخدم وكلمة المرور كالتالي 
  print("Incorrect username or password") # سيتم طباعة الجملة ثم تكرار الحلقة الى ان يتم كتابته بشكل صحيح

print ("login successful") # في حال تم البرنامج يتم طباعةالجملة


