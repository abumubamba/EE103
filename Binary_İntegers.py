sayı=int(input("Bir sayı giriniz: "))
binary=""
while sayı>0:
    remainder=sayı%2
    binary=str(remainder)+binary
    sayı=sayı//2
print("girilen sayının binary kodu: ",binary,)

x=0
for i in range (10):
    x = x + 0.1

print(x)
