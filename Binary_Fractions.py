sayı=float(input("ondalıklı bir sayı giriniz (opsiyonel): "))
tam=int(sayı)
kesir=sayı-tam
if tam==0:
    binary="0"
else:
    binary=""
    while tam >0:
        remainder=tam%2
        binary=str(remainder)+binary
        tam=tam//2
    binary_2=""
    while kesir >0:
        kesir*=2
        bit=int(kesir)
        binary_2+= str(bit)
        kesir-=bit
if binary_2!="":
    binary_3=f"{binary}.{binary_2}"
else:
    binary_3=binary

print(binary_3)