# ������������ ������ � 2
# ������� 3, ������� 1
# ��� �������� a � b �������� c = max(a,b), ���� a>0 ��� c =min(a,b), ���� a <= 0
a = int(input())
b = int(input())
if a > 0:
    c = max(a,b)
    print(c)
else:
    if a <= 0:
        c = min(a,b)
        print(c)
        
