# If
nilai = 80
if nilai >= 70:
    print("Lulus")

# If Else
if nilai >= 70:
    print("Lulus")
else:
    print("Tidak Lulus")

# If Elif Else
str_input = input("Enter Your Day: ")

hari_ini = "Minggu"

if(hari_ini == "Senin"):
    print("Saya akan kuliah")
elif(hari_ini == "Selasa"):
    print("Saya akan kuliah")
elif(hari_ini == "Rabu"):
    print("Saya akan kuliah")
elif(hari_ini == "Kamis"):
    print("Saya akan kuliah")
elif(hari_ini == "Jumat"):
    print("Saya akan kuliah")
elif(hari_ini == "Sabtu"):
    print("Saya akan kuliah")
elif(hari_ini == "Minggu"):
    print("Saya akan libur")

str_input = input("Enter Your Grade: ")
print("Inputan User: ", str_input, type(str_input))

# Keyword else
str_input = input("Enter Your Grade: ")
grade = int(str_input)

if grade >= 100:
    print('Perfect')
elif grade >= 85:
    print('Awesome')
elif grade >= 65:
    print('Passed The Exam')
else:
    print('Failed')

# Kondisi Bercabang
str_input = input("Enter Your Number: ")
number = int(str_input)

if number >= 100:
    print('Perfect')
elif number >= 85:
    print('Awesome')
elif number >= 65:
    print('Passed The Exam')

    if number <= 70:
        print('But you need to improve it')
    else:
        print('with ok grade')

else:
    print('Below the passing grade')