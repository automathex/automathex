#!/usr/bin/python

from tkinter import *
from sympy import *
x, y, z, t = symbols('x y z t')
import tkinter.tix as tx


def formate(txt):
    txt=txt.replace("\\frac","\\dfrac")
    if not("left" in txt):
        txt=txt.replace("(","\\left(")
    if not "right" in txt:
        txt=txt.replace(")","\\right)")
    txt=txt.replace("log",'ln')
    return txt


def signe_infini(a):
    if a=="\\infty":
        return "+"+a
    else:
        return a

###############################################################################################################
############################             Nombres complexes
###############################################################################################################

def forme_trigo(z):
    txt="z=$"+latex(z)+"$\\\\"
    txt=txt+"$r=\sqrt{a^2+b^2}=\sqrt{("+latex(re(z))+")^2+("+latex(im(z))+")^2}="+latex(abs(z))+"$\\\\"
    txt=txt+"$cos\\theta=\dfrac{a}{r}=\dfrac{"+latex(re(z))+"}{"+latex(abs(z))+"}$"
    if latex(re(z)/abs(z))!="\\frac{"+latex(re(z))+"}{"+latex(abs(z))+"}":
        txt=txt+" = $"+latex(re(z)/abs(z))+"$"
    txt=txt+"    et $sin\\theta=\dfrac{b}{r}=\dfrac{"+latex(im(z))+"}{"+latex(abs(z))+"}$"
    if latex(im(z)/abs(z))!="\\frac{"+latex(im(z))+"}{"+latex(abs(z))+"}":
        txt=txt+" = $"+latex(im(z)/abs(z))+"$"
    txt=txt+"\\\\Ainsi $\\theta="+latex(arg(z))+"$ modulo $2\\pi$\\\\"

    if arg(z)>=0:
        txt=txt+"On obtient donc $z="+latex(abs(z))+"(cos"+latex(arg(z))+"+i sin"+latex(arg(z))+")$\\\\"
        txt=txt+"et $z="+latex(abs(z))+"e^{i"+latex(arg(z))+"}$\\\\"
    else:
        txt=txt+"On obtient donc $z="+latex(abs(z))+"(cos("+latex(arg(z))+")+i sin("+latex(arg(z))+"))$\\\\"
        txt=txt+"et $z="+latex(abs(z))+"e^{-i"+latex(-arg(z))+"}$\\\\"


    return formate(txt)+"\\\\"



class Interface_complexe(Frame):


    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=250, **kwargs)
        self.pack(fill=BOTH)


        # Création de nos widgets

#######
        self.label1=Label(self,text="entrer le nombre complexe")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=25)
        self.entre1.place(x=5,y=20)
        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)
        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)

    ##
    def go(self):

        if self.entre1.get()!="" :

            z=self.entre1.get()
            z=z.replace("i","I")
            txt=forme_trigo(sympify(z))
        else:
            txt="Il faut entrer un nombre complexe\\\\"
        self.textBox.insert(END,txt)


    ##
    def quitter(self):
        self.quit()
    ##
    ##
    def effacer(self):
        self.textBox.delete(1.0,END)

###############################################################################################################
###################                               Trinome
###############################################################################################################

def coefficients(p):
    coeff=p.as_coefficients_dict()
    return coeff[x**2],coeff[x],coeff[1]

def est_un_carre(x):
    y=sqrt(x)
    return y==int(y)

def affiche_avec_parenthese(x):
        if x<0:
            return "("+latex(x)+")"
        else:
            return latex(x)

def afficher_calcul_delta(p):
    a,b,c=coefficients(p)

    d=b**2-4*a*c
    txt="$\Delta=b^2-4ac="+affiche_avec_parenthese(b)+"^2-"+"4\\times"+affiche_avec_parenthese(a)+" \\times"+affiche_avec_parenthese(c)+"="+latex(d)+"$\\\\"
    return formate(txt)

def afficher_nombre_solution(p,ensemble):
    if discriminant(p)<0:
        if ensemble=="R":
            txt="$\Delta<0$ donc l'équation $"+latex(p)+"=0 $"+ " n'admet pas de solution \\\\"
        else:
            txt="$\Delta<0$ donc l'équation $"+latex(p)+"=0$ "+ " admet deux solutions complexes conjuguées :\\\\"

    elif discriminant(p)==0:
        txt="$\Delta=0$ donc l'équation $ "+latex(p)+ "=0$ admet une unique solution : \\\\"
    else:
        txt="$\Delta>0 $ donc l'équation $"+latex(p)+ "=0$ admet deux solutions réelles :\\\\"
    return txt

def afficher_x0(p,ensemble):
    a,b,c=coefficients(p)
    if ensemble=="R":
        txt="$x_0="
    else:
        txt="$z_0="
    txt=txt+"$-\\frac{b}{2a}=\dfrac{"+latex(-b)+"}{"+latex(2*a)+"}="+latex(-b/(2*a))+" \\\\$"

    return formate(txt)

def afficher_x1(p):
    a,b,c=coefficients(p)
    d=discriminant(p)
    txt="$x_1=\\frac{-b-\sqrt{\Delta}}{2a}=\dfrac{-"+affiche_avec_parenthese(b)+"-\sqrt{"+latex(d)+"}"+"}{2\\times"+affiche_avec_parenthese(a)+"}="
    txt=txt+"\\frac{"+latex(-b-sqrt(d))+"}{"+latex(2*a)+"}="
    txt=txt+latex((-b-sqrt(d))/(2*a))
    return formate(txt)+"$\\\\"

def afficher_x2(p):
    a,b,c=coefficients(p)
    d=discriminant(p)
    txt="$x_2=\\frac{-b+\sqrt{\Delta}}{2a}=\dfrac{-"+affiche_avec_parenthese(b)+"+\sqrt{"+latex(d)+"}"+"}{2\\times"+affiche_avec_parenthese(a)+"}="
    txt=txt+"\\frac{"+latex(-b+sqrt(d))+"}{"+latex(2*a)+"}="
    txt=txt+latex((-b+sqrt(d))/(2*a))
    return formate(txt)+"$\\\\"

def afficher_z1(p):
    a,b,c=coefficients(p)
    d=discriminant(p)
    txt="$z_1=\\frac{-b-{i}\sqrt{\Delta}}{2a}=\dfrac{-"+affiche_avec_parenthese(b)+"-{i}\sqrt{"+str(-d)+"}}"+"{2\\times"+affiche_avec_parenthese(a)+"}="
    txt=txt+latex((-b-sqrt(d))/(2*a))
    return formate(txt)+"$\\\\"

def afficher_z2(p):
    a,b,c=coefficients(p)
    d=discriminant(p)
    txt="$z_2=\\frac{-b+{i}\sqrt{\Delta}}{2a}=\dfrac{-"+affiche_avec_parenthese(b)+"+{i}\sqrt{"+str(-d)+"}}"+"{2\\times"+affiche_avec_parenthese(a)+"}="
    txt=txt+latex((-b+sqrt(d))/(2*a))
    return formate(txt)+"$\\\\"

def afficher_solution(p,ensemble):
    if discriminant(p)<0:
        if ensemble=="R":
            txt=""
        else:
            txt=afficher_z1(p)+"\n"+afficher_z2(p)

    elif discriminant(p)==0:
        txt=afficher_x0(p)
    else:
        txt=afficher_x1(p)+"\n"+afficher_x2(p)

    return txt

class Interface_trinome(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=250, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        ####
        self.label1=Label(self,text="entrer la valeur de a")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=5)
        self.entre1.place(x=150,y=0)
        self.label2=Label(self,text="entrer la valeur de b")
        self.label2.place(x=0,y=20)
        self.entre2=Entry(self,width=5)
        self.entre2.place(x=150,y=20)
        self.label3=Label(self,text="entrer la valeur de c")
        self.label3.place(x=0,y=40)
        self.entre3=Entry(self,width=5)
        self.entre3.place(x=150,y=40)

        ####
        self.label00=Label(self,text="     OU     ",bg="red",width=25)
        self.label00.place(x=0,y=70)
        ########
        self.label4=Label(self,text="entrer la valeur de a")
        self.label4.place(x=0,y=100)
        self.entre4=Entry(self,width=5)
        self.entre4.place(x=150,y=100)
        self.label5=Label(self,text="entrer la valeur de x1")
        self.label5.place(x=0,y=120)
        self.entre5=Entry(self,width=5)
        self.entre5.place(x=150,y=120)
        self.label6=Label(self,text="entrer la valeur de x2")
        self.label6.place(x=0,y=140)
        self.entre6=Entry(self,width=5)
        self.entre6.place(x=150,y=140)
        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)
        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)
        self.varrb=StringVar(None,'R')
        self.rb1=Radiobutton(self,variable=self.varrb,text="Réel",value="R",takefocus=1)
        self.rb1.place(x=620,y=30)
        self.rb2=Radiobutton(self,variable=self.varrb,text="Complexe",value="C",takefocus=0)
        self.rb2.place(x=620,y=50)



    def go(self):
        if (self.entre1.get()!="") and self.entre2.get()!="" and self.entre3.get()!="":
            a=sympify(self.entre1.get())
            b=sympify(self.entre2.get())
            c=sympify(self.entre3.get())
            ensemble=self.varrb.get()
            p=a*x**2+b*x+c
            txt=afficher_calcul_delta(p)+"\n"+afficher_nombre_solution(p,ensemble)+"\n"+afficher_solution(p,ensemble)+"\n"
            self.textBox.insert(END,txt)
        elif (self.entre4.get()!="") and self.entre5.get()!="" and self.entre6.get()!="":
            a=sympify(self.entre4.get())
            x1=sympify(self.entre5.get())
            x2=sympify(self.entre6.get())
            b=-(x1+x2)*a
            c=x1*x2*a
            ensemble=self.varrb.get()
            p=a*x**2+b*x+c
            txt=afficher_calcul_delta(p)+"\n"+afficher_nombre_solution(p,ensemble)+"\n"+afficher_solution(p,ensemble)+"\n"
            self.textBox.insert(END,txt)
        else:
            txt="Il manque des données\n"
            self.textBox.insert(END,txt)



    def quitter(self):
        self.quit()

    def effacer(self):
        self.textBox.delete(1.0,END)

###############################################################################################################
############################             Limites
###############################################################################################################

def limite_polynome(f,a):
    txt="$ "+latex(f)+"="
    txt=txt+""+latex(LM(f))+"("+latex(expand(f/LM(f)))+")"+"$"
    txt=txt+"on sait que $\lim_{x \\to " + latex(a)+"}"+latex(expand(f/LM(f)))+"="+signe_infini(latex(limit(f/LM(f),x,a)))+"$\\\\"
    txt=txt+"or $\lim_{x \\to " + signe_infini( latex(a))+"}"+latex(LM(f))+"="+signe_infini(latex(limit(LM(f),x,a)))+"$\\\\"
    txt=txt+"Ainsi  $\lim_{x \\to " +  signe_infini( latex(a))+"}"+latex(f)+"="+signe_infini(latex(limit(f,x,a)))+"$\\\\"
    return formate(txt)+"\\\\"



def limite_quotient(f,g,a):
    txt="$ "+latex(f/g)+"="
    txt=txt+"\dfrac{"+latex(LM(f))+"("+latex(expand(f/LM(f)))+")}{"+latex(LM(g))+"("+latex(expand((g)/LM(g)))+")}="
    if degree(f)>degree(g):
        x_num=x**(degree(f)-degree(g))
        x_denom=""
    elif degree(f)<degree(g):
        x_num=""
        x_denom=x**(degree(g)-degree(f))
    else:
        x_num=""
        x_denom=""
    txt=txt+"\dfrac{"+latex(x_num)+"("+latex(expand(f/LM(f)))+")}{"+latex(x_denom)+"("+latex(expand((g)/LM(g)))+")}$ \\\\"

    if x_num !="":
        txt=txt+"On sait que $\lim_{x \\to " + latex(a)+"}"+latex(expand(f/LM(f)))+"="+signe_infini(latex(limit(f/LM(f),x,a)))+"$"
        txt=txt+"et $\lim_{x \\to " + signe_infini( latex(a))+"}"+latex(x_num)+"="+signe_infini(latex(limit(x_num,x,a)))+"$ "
        txt=txt+"donc $\lim_{x \\to " + signe_infini( latex(a))+"}"+latex(x_num)+"("+latex(expand(f/LM(f)))+")="+signe_infini(latex(limit(f/LM(f),x,a)*limit(x_num,x,a)))+"$(par produit)\\\\"
        txt=txt+"De plus $\lim_{x \\to " + signe_infini(latex(a))+"}"+latex(expand(g/LM(g)))+"="+signe_infini(latex(limit(g/LM(g),x,a)))+"$"

    elif x_denom!="":
        txt=txt+"On sait que $\lim_{x \\to " + latex(a)+"}"+latex(expand(g/LM(g)))+"="+signe_infini(latex(limit(g/LM(g),x,a)))+"$"
        txt=txt+"et $\lim_{x \\to " + signe_infini( latex(a))+"}"+latex(x_denom)+"="+signe_infini(latex(limit(x_denom,x,a)))+"$ "
        txt=txt+"donc $\lim_{x \\to " + signe_infini( latex(a))+"}"+latex(x_denom)+"("+latex(expand(g/LM(g)))+")="+signe_infini(latex(limit(g/LM(g),x,a)*limit(x_denom,x,a)))+"$(par produit)\\\\"
        txt=txt+"De plus $\lim_{x \\to " + signe_infini(latex(a))+"}"+latex(expand(f/LM(f)))+"="+signe_infini(latex(limit(f/LM(f),x,a)))+"$"

    txt=txt+" Ainsi  $\lim_{x \\to " +  signe_infini( latex(a))+"}"+latex(f/g)+"="+signe_infini(latex(limit(f/g,x,a)))+"$(par quotient)\\\\"
    return formate(txt)+"\\\\"


class Interface_limite(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=250, **kwargs)
        self.pack(fill=BOTH)



        # Création de nos widgets


        ######
        self.label1=Label(self,text="entrer la fonction f")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=25)
        self.entre1.place(x=5,y=20)
        ##
        self.label2=Label(self,text="entrer la fonction g")
        self.label2.place(x=0,y=40)
        self.entre2=Entry(self,width=25)
        self.entre2.place(x=5,y=60)
        ##
        self.varrb3=StringVar(None,"+inf")
        self.rb3=Radiobutton(self,variable=self.varrb3,text="Limite en +oo",value="+inf")
        self.rb3.place(x=0,y=80)
        self.rb4=Radiobutton(self,variable=self.varrb3,text="Limite en -oo",value="-inf")
        self.rb4.place(x=0,y=100)
        ##
        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)
        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)
        self.varrb=StringVar(None,"1")
        self.rb1=Radiobutton(self,variable=self.varrb,text="Limite d'un polynome",value="1",takefocus=1)
        self.rb1.place(x=620,y=30)
        self.rb2=Radiobutton(self,variable=self.varrb,text="Limite d'un quotient",value="2",takefocus=0)
        self.rb2.place(x=620,y=50)




    def go(self):

        if self.varrb3.get()=="+inf":
            a=+oo
        else:
            a=-oo

        if self.varrb.get()=="1" and (self.entre1.get()!="") :
            txt=limite_polynome(sympify(self.entre1.get()),a)
            self.textBox.insert(END,txt)
        elif self.varrb.get()=="2" and (self.entre1.get()!="") and self.entre2.get()!="":
            txt=limite_quotient(sympify(self.entre1.get()),sympify(self.entre2.get()),a)
            self.textBox.insert(END,txt)
        else:
            txt="Il manque des données\\\\"
            self.textBox.insert(END,txt)


    def quitter(self):
        self.quit()

    def effacer(self):
        self.textBox.delete(1.0,END)


###############################################################################################################
############################             Derivation
###############################################################################################################

def deriver_produit(u,v):
    txt="$f(x)=("+latex(u)+")\\times("+latex(v)+")$\\\\"
    txt=txt+"La fonction est de la forme $u(x)\\times{v(x)} $\\\\"
    txt=txt+"avec $u(x)="+latex(u)+"$ , $v(x)="+latex(v)+"$, $u'(x)="+latex(diff(u,x))+"$ et $v'(x)="+latex(diff(v,x))+"$\\\\"
    txt=txt+"$f'(x)$ est de la forme $ u'(x)\\times{v(x)}+v'(x)\\times{u(x)}$\\\\"
    txt=txt+"$f'(x)=("+latex(diff(u,x))+")\\times("+latex(v)+")+("+latex(diff(v,x))+")\\times("+latex(u)+")$\\\\"
    txt=txt+"$f'(x)="+latex(expand(diff(u,x)*v))+"+("+latex((expand(diff(v,x)*u)))+")$\\\\"
    txt=txt+"$f'(x)="+latex(expand(diff(u,x)*v+(diff(v,x)*u)))
    return formate(txt)+"$\\\\"

def deriver_quotient(u,v):
    txt="$f(x)=\dfrac{"+latex(u)+"}{"+latex(v)+"}$\\\\"
    txt=txt+"La fonction est de la forme $\dfrac{u(x)}{v(x)}$ \\\\"
    txt=txt+"avec $u(x)="+latex(u)+"$ , $v(x)="+latex(v)+"$, $u'(x)="+latex(diff(u,x))+"$ et $v'(x)="+latex(diff(v,x))+"$\\\\"
    txt=txt+"$f'(x)$ est de la forme $\dfrac{u'(x)\\times{v(x)}-v'(x)\\times{u(x)}}{v^2(x)}$\\\\"
    txt=txt+"$f'(x)=\dfrac{("+latex(diff(u,x))+")\\times("+latex(v)+")-("+latex(diff(v,x))+")\\times("+latex(u)+")}{("+latex(v)+")^2}$\\\\"
    txt=txt+"$f'(x)=\dfrac{"+latex(expand(diff(u,x)*v))+latex(-expand(diff(v,x)*u))+"}{("+latex(v)+")^2}$\\\\"
    txt=txt+"$f'(x)=\dfrac{"+latex(expand(diff(u,x)*v)-expand(diff(v,x)*u))+"}{("+latex(v)+")^2}"
    return formate(txt)+"$\\\\"

def deriver_puissance(u,n):
    txt="$f(x)=("+latex(u)+")^{"+str(n)+"}$ \\\\"
    txt=txt+"La fonction est de la forme $u(x)^{"+str(n)+"}$"
    txt=txt+"avec $u(x)="+latex(u)+"$, $u'(x)="+latex(diff(u,x))+"$\\\\"
    txt=txt+"$f'(x)$ est de la forme $"+str(n)+"\\times u'(x)\\times(u(x))^{"+str(n-1)+"}$\\\\"
    txt=txt+"$f'(x)="+str(n)+"\\times{("+latex(diff(u,x))+")}\\times("+latex(u)+")^{"+str(n-1)+"}"
    txt=txt+"=("+latex(n*diff(u,x))+")\\times("+latex(u)+")^{"+str(n-1)+"}"
    return formate(txt)+"$\\\\"


class Interface_derivee(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=250, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        ######
        self.label1=Label(self,text="entrer la fonction u")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=25)
        self.entre1.place(x=5,y=20)

        self.label2=Label(self,text="entrer la fonction v")
        self.label2.place(x=0,y=40)
        self.entre2=Entry(self,width=25)
        self.entre2.place(x=5,y=60)

        self.label3=Label(self,text="entrer la valeur de n")
        self.label3.place(x=0,y=80)
        self.entre3=Entry(self,width=25)
        self.entre3.place(x=5,y=100)
        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)

        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)

        self.varrb=StringVar(None,"1")
        self.rb1=Radiobutton(self,variable=self.varrb,text="Dériver un produit",value="1")
        self.rb1.place(x=620,y=30)
        self.rb1.select()

        self.rb2=Radiobutton(self,variable=self.varrb,text="Dériver un quotient",value="2")
        self.rb2.place(x=620,y=50)

        self.rb3=Radiobutton(self,variable=self.varrb,text="Dériver une puissance",value="3")
        self.rb3.place(x=620,y=70)




    def go(self):

        if self.varrb.get()=="1" and (self.entre1.get()!="") and self.entre2.get()!="":
            txt=deriver_produit(sympify(self.entre1.get()),sympify(self.entre2.get()))

        elif self.varrb.get()=="2" and (self.entre1.get()!="") and self.entre2.get()!="":
            txt=deriver_quotient(sympify(self.entre1.get()),sympify(self.entre2.get()))

        elif self.varrb.get()=="3" and (self.entre1.get()!="") and self.entre3.get()!="":
            txt=deriver_puissance(sympify(self.entre1.get()),int(self.entre3.get()))
        else:
            txt="Il manque des données\\\\"
        self.textBox.insert(END,txt)



    def quitter(self):
        self.quit()

    def effacer(self):
        self.textBox.delete(1.0,END)



###############################################################################################################
############################             Binomial
###############################################################################################################

def binompdf(n,p,k):
    return binomial(n,k)*(p**k)*((1-p)**(n-k))

def affiche_avec_parenthese(x):
        if x!=int(x):
            return "("+latex(x)+")"
        else:
            return latex(x)


def phrase_binom(n,p):
    txt="On répète $"+latex(n)+"$ fois des expériences aléatoires identiques et de manière indépendante. Chaque expérience possède deux issues. La probabilité de succès est de $"+latex(p)+"$.\\\\"
    txt=txt+"La variable aléatoire $X$ qui compte le nombre de succès suit donc une loi binomiale de paramètres $ "+latex(n)+"$ et $"+latex(p)+"$\\\\"
    return formate(txt)
def calcul_binompdf(n,p,k,decimal):
    txt="$P(X=k)=\\begin{pmatrix} n  \\\\k \\end{pmatrix}\\times p^k \\times (1-p)^{n-k}$\\\\"
    txt=txt+"Donc $P(X="+latex(k)+")=\\begin{pmatrix}"+latex(n)+"  \\\\"+latex(k)+" \\end{pmatrix}\\times"+affiche_avec_parenthese(p)+"^"+latex(k)+" \\times(1-"+latex(p)+")^"+latex(n-k)+"$\\\\"
    txt=txt+"Ainsi $P(X="+latex(k)+")\\approx"+str(round(binompdf(n,p,k),decimal))+"$ \\quad \\quad à $10^{-"+latex(decimal)+"}$ près\\\\"
    return formate(txt)



class Interface_binomial(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=260, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        ######
        self.label1=Label(self,text="entrer la valeur de n")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=25)
        self.entre1.place(x=5,y=20)

        self.label2=Label(self,text="entrer la valeur de p")
        self.label2.place(x=0,y=40)
        self.entre2=Entry(self,width=25)
        self.entre2.place(x=5,y=60)

        self.label3=Label(self,text="entrer la valeur de k")
        self.label3.place(x=0,y=80)
        self.entre3=Entry(self,width=25)
        self.entre3.place(x=5,y=100)

        self.label4=Label(self,text="entrer la valeur de précision")
        self.label4.place(x=0,y=120)
        self.var4=StringVar()
        self.var4.set("3")
        self.entre4=Entry(self,textvariable=self.var4,width=25)
        self.entre4.place(x=5,y=140)

        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)

        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)




    def go(self):

        if (self.entre1.get()!="") and self.entre2.get()!="" and self.entre3.get()!="":
            txt=phrase_binom(int(self.entre1.get()),sympify(self.entre2.get()))
            txt=txt+calcul_binompdf(int(self.entre1.get()),sympify(self.entre2.get()),int(self.entre3.get()),int(self.entre4.get()))

        else:
            txt="Il manque des données\\\\"
        self.textBox.insert(END,txt)



    def quitter(self):
        self.quit()

    def effacer(self):
        self.textBox.delete(1.0,END)


def effacer():
    for c in fen1.winfo_children():
        c.destroy()


###############################################################################################################
############################             TVI
###############################################################################################################

def solution(f,a,c,precision):
    expr=sympify(f-c)

    if a==-oo:
        return latex(round(nsolve(expr,-9999999999),precision)).replace(".",",")
    elif expr.subs(x,a)==zoo:
        return latex(round(nsolve(expr,a+0.0000000001),precision)).replace(".",",")
    else:
        return latex(round(nsolve(expr,a),precision)).replace(".",",")



def max(f,a,b):
    if limit(f,x,a)>limit(f,x,b):
        return f.subs(x,a)
    else:
        return f.subs(x,b)

def min(f,a,b):
    if limit(f,x,a)<limit(f,x,b):
        return limit(f,x,a)
    else:
        return limit(f,x,b)


def tvi(f,a,b,c,precision):
    intervalle=Interval.open(a,b)

    if is_monotonic(f,intervalle) and c<max(f,a,b) and c>min(f,a,b):
        txt="Soit $f$ la fonction définie sur $]"+latex(a)+";"+signe_infini(latex(b))+"[$ par $f(x)="+latex(sympify(f))+"$"
        txt=txt+"\\begin{itemize}"
        txt=txt+"\\item La fonction $f$ est continue sur $]"+latex(a)+";"+signe_infini(latex(b))+"[$"
        if is_decreasing(f,intervalle):
            txt=txt+"\\item La fonction $f$ est strictement décroissante sur $]"+latex(a)+";"+signe_infini(latex(b))+"[$"
        if is_increasing(f,intervalle):
            txt=txt+"\\item La fonction $f$ est strictement croissante sur $]"+latex(a)+";"+signe_infini(latex(b))+"[$"
        if a==oo or a==-oo or limit(f,x,a).is_infinite:
            txt=txt+"\\item On sait que $\lim_{x \\to " + signe_infini(latex(a))+"}"+latex(f)+"="+signe_infini(latex(limit(f,x,a)))+"$"
        else:
            txt=txt+"\item On sait que $f("+latex(a)+")="+latex(f.subs(x,a).evalf())+"$"

        if b==oo or b==-oo or limit(f,x,b).is_infinite:
            txt=txt+" et que $\lim_{x \\to " + signe_infini(signe_infini(latex(b)))+"}"+latex(f)+"="+signe_infini(latex(limit(f,x,b)))+"$\\\\"
        else:
            txt=txt+" et que $f("+latex(b)+")="+latex(f.subs(x,b).evalf())+"$\\\\"

        txt=txt+"On voit que $"+latex(c)+"\in ]"+latex(min(f,a,b))+";"+signe_infini(latex(max(f,a,b)))+"[$"
        txt=txt+"\\\\D'après le corollaire du théorème des valeurs intermédiaires, il existe un unique $\\alpha$ dans l'intervalle  $]"+latex(a)+";"+signe_infini(latex(b))+"[$ vérifiant $f(\\alpha)="+latex(c)+"$\\\\"
        txt=txt+"A la calculatrice, on trouve $\\alpha \\approx "+solution(f,a,c,precision)+"$\\\\"


        txt=txt+"\end{itemize}"
    elif c<max(f,a,b) and c>min(f,a,b):
        txt="La fonction f n'est pas monotone sur $]"+latex(a)+";"+latex(b)+"[$\\\\"
    else:
        txt=latex(c)+" n'est pas dans l'intervalle image."

    return formate(txt)


class Interface_tvi(Frame):

    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=800, height=250, **kwargs)
        self.pack(fill=BOTH)

        # Création de nos widgets
        ######
        self.label1=Label(self,text="entrer la fonction f")
        self.label1.place(x=0,y=0)
        self.entre1=Entry(self,width=25)
        self.entre1.place(x=5,y=20)

        self.label2=Label(self,text="entrer la valeur de a")
        self.label2.place(x=0,y=40)
        self.entre2=Entry(self,width=25)
        self.entre2.place(x=5,y=60)

        self.label3=Label(self,text="entrer la valeur de b")
        self.label3.place(x=0,y=80)
        self.entre3=Entry(self,width=25)
        self.entre3.place(x=5,y=100)

        self.label4=Label(self,text="entrer la valeur de c")
        self.label4.place(x=0,y=120)
        self.var4=StringVar()
        self.var4.set("0")
        self.entre4=Entry(self,textvariable=self.var4,width=25)
        self.entre4.place(x=5,y=140)

        self.label5=Label(self,text="entrer la valeur de précision")
        self.label5.place(x=0,y=160)
        self.var5=StringVar()
        self.var5.set("3")
        self.entre5=Entry(self,textvariable=self.var5,width=25)
        self.entre5.place(x=5,y=180)

        self.btn1=Button(self,text="OK",command=self.go)
        self.btn1.place(x=50,y=220)
        self.btn2=Button(self,text="Quitter",command=self.quitter)
        self.btn2.place(x=100,y=220)
        self.btn3=Button(self,text="Effacer",command=self.effacer)
        self.btn3.place(x=200,y=220)

        self.textBox = Text(self, height=10, width=50)
        self.textBox.place(x=200,y=0)




    def go(self):

        if (self.entre1.get()!="") and self.entre2.get()!="" and self.entre3.get()!="" and (self.entre4.get()!=""):
            txt=tvi(sympify(self.entre1.get()),sympify(self.entre2.get()),sympify(self.entre3.get()),sympify(self.entre4.get()),int(self.entre5.get()))


        else:
            txt="Il manque des données\\\\"
        self.textBox.insert(END,txt)



    def quitter(self):
        self.quit()

    def effacer(self):
        self.textBox.delete(1.0,END)


def effacer():
    for c in fen1.winfo_children():
        c.destroy()

#####################################################################################################
############################# Interface principale
####################################################################################################


root=tx.Tk()

root.geometry("810x310+0+10")
root.title ("autolatex")

nb=tx.NoteBook(root)
nb.pack(fill=tx.BOTH, expand=1)

nb.add("tab1",label="Dériver")
interface1 = Interface_derivee(nb.tab1)

nb.add("tab2",label="Limites")
interface2=Interface_limite(nb.tab2)

nb.add("tab3",label="Trinôme")
interface3=Interface_trinome(nb.tab3)

nb.add("tab4",label="Complexes")
interface4=Interface_complexe(nb.tab4)

nb.add("tab5",label="Loi binomiale")
interface5=Interface_binomial(nb.tab5)

nb.add("tab6",label="TVI")
interface6=Interface_tvi(nb.tab6)
root.mainloop()
root.destroy()
