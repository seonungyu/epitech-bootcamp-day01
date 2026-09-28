while 1:
 n,s=input().split(" ",1);n=int(n)
 if n==0:break
 print(n if n>=42 or set(s)&set("aeiouAEIOU")else s)
