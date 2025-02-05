# Comece executando as instruções de atribuição:

# >>> s1 = 'ant'
s1 = 'ant'
# >>> s2 = 'bat'
s2 = 'bat'
# >>> s3 = 'cod'
s3 = 'cod'

#Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de avaliar para:
# 'ant bat cod'
print(s1 + ' ' + s2 + ' ' + s3)

# ant ant ant ant ant ant ant ant ant ant'
print((s1 + " ") * 10)

# 'ant bat bat cod cod cod'
print(s1 + ' ' + (s2 +' ') * 2 + (s3 + " ") * 3)

# 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
print((s1 + ' ' + s2 + ' ') * 7)

# 'batbatcod batbatcod batbatcod batbatcod batbatcod'
print((((s2 * 2) + s3) + " " )* 5)