
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")


def equation(request):
    quad=request.POST.get("quad","off")
    linear=request.POST.get("linear","off")

    if quad=="clicked":
        return render(request,"quadratic.html")
    if linear=="clicked":
        return render(request,"linear.html")


def quadsolver(request):
    
    a=int(request.POST.get("a","0"))
    b=int(request.POST.get("b","0"))
    c=int(request.POST.get("c","0"))

    if(a==0):
      return HttpResponse("Not A Quadratic Equation")
    else:
      D=(b**2)-(4*a*c)
      if D>0:
          x1=(-b+(D)**(1/2))/(2*a)
          x2=(-b-(D)**(1/2))/(2*a)

          v={
          "a":a,
          "b":b,
          "c":c,
          "x1":x1,
          "x2":x2,
          }
          return render(request,"quadraticsolution.html",v)

      elif D==0:
          x1=-b/(2*a)
          x2=-b/(2*a)

          v={
          "a":a,
          "b":b,
          "c":c,
          "x1":x1,
          "x2":x2,
          }
          return render(request,"quadraticsolution.html",v)

      else:
        D=-D
        real=str(-b/(2*a))
        img=str(((D)**(1/2))/(2*a))
        x1= real + "+"+img +"i"
        x2= real +"-"+img +"i"
        v={
          "a":a,
          "b":b,
          "c":c,
          "x1":x1,
          "x2":x2,
          }
        return render(request,"quadraticsolution.html",v)

def linearsolver(request):
   a1=int(request.POST.get("a1","0"))
   b1=int(request.POST.get("b1","0"))
   c1=int(request.POST.get("c1","0"))
   a2=int(request.POST.get("a2","0"))
   b2=int(request.POST.get("b2","0"))
   c2=int(request.POST.get("c2","0"))

   factor1=a1
   factor2=a2

   a11=a1*a2
   b11=b1*a2
   c11=c1*a2

   a22=a2*a1
   b22=b2*a1
   c22=c2*a1

   y=-(c11-c22)/(b11-b22)
   x=(-c11-b11*y)/a11

   v={
      "a1":a1,
      "b1":b1,
      "c1":c1,
      "a2":a2,
      "b2":b2,
      "c2":c2,
      "x":x,
      "y":y
   }
   return render(request,"linearsolution.html",v)

def aboutus(request):
   return render( request ,"aboutus.html")