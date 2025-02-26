#ipo
#input
#process
#output

L = float(input("Lợi nhuận sau thuế: "))
n = int(input("Số sổ phần: "))
r = float(input("tỉ lệ cổ tức cho mỗi cổ phần : "))

T = (n * r * L)/100
print(f"Tổng Số tiền cty phải chia cho mỗi cổ đông là: {round(T, 2)}")