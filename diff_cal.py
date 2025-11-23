import time
import sympy as sp
import random
import tabulate
import matplotlib.pyplot as plt
def sleep():
    time.sleep(1)
print("""\033[35m
_________________________________________
|   1.monotonicity                      |
|   2.Extrema                           |
|   3.Absolute Extrema                  |
|   4.concavity                         |
|   5.point of inflection               |
|Give function in                       |
|       square root -> sqrt             |
|       add,sub,div,mul ->+,-,/,*       |
|       exponential,power->exp,** or ^  |
_________________________________________\033[0m
""")

funcWithInterval = input("Enter the function:")#get input of function
if "&" in funcWithInterval:
    func, interval = tuple(funcWithInterval.split("&"))#split the interval and function by &
    interval = list(interval)#convert string to list
else:
    interval : list =[]#no input interval
    func=funcWithInterval#store the input to function
func=func.replace("^","**")#replace ^ in function to **
x = sp.Symbol('x')#it denote the variable of the function
f = sp.sympify(func)#pass function for sympify

df = sp.diff(f, x)#deff method is used to differentiate the function
sleep()
print(f'df={df.evalf()}')
sleep()
print("\033[31mDifferentation completed......\033[0m")
critical_point = sp.solve(sp.Eq(df, 0), x)#solve function solve
'''for i in range(len(critical_point)):
    if type(critical_point[0])==type(complex()):
        print("it is complex number")
        os.system("exit")
        exit()
    critical_point[i]=critical_point[i].evalf()'''
c_p=list(critical_point)
sleep()
print("\033[32mcritical point :\033[0m",critical_point)
if len(interval)==0:
    critical_point.insert(0, float('-inf'))
    critical_point.append(float('inf'))
else:
    critical_point.insert(0,float(interval[0]))
    critical_point.append(float(interval[-1]))
monotonicity = []
local_extrema = []
concavity = []
inflection = []

# -------------------------
# MONOTONICITY
# -------------------------
for i in range(len(critical_point) - 1):
    if i==len(critical_point)-2:
        test_point=critical_point[i]+1
    else:
        test_point=critical_point[i+1]-1
        if test_point==critical_point[i]:
            while True:
                test_point=random.uniform(critical_point[i],critical_point[i+1])
                if critical_point[i]<test_point<critical_point[i+1]:
                    break
    sub = df.subs(x, test_point)

    if float(sub )>= 0:
        monotonicity.append({
            "interval":f"{critical_point[i]}<x<{critical_point[i+1]}",
            "f'(x)":float(sub),
            "sign":'+',
            "func goes":'increasing',
            "at x=":critical_point[i+1],
            "testpnt":test_point
        })
    else:
        monotonicity.append({
            "interval": f"{critical_point[i]}<x<{critical_point[i + 1]}",
            "f'(x)": float(sub),
            "sign": '-',
            "func goes": 'decreasing',
            "at x=": critical_point[i + 1],
            "testpnt":test_point
        })
sleep()
print("\033[31mmonotonocity completed...\033[0m")
# -------------------------
# LOCAL EXTREMA
# -------------------------
for i in range(0, len(monotonicity) - 1):

    if monotonicity[i]["sign"] == '+' and monotonicity[i+1]["sign"] == '-':
        cp = critical_point[i+1]
        local_extrema.append({
            "x=": cp,
            "f(x) attains": "local maximum",
            "value": float(f.subs(x, cp)),
        })

    elif monotonicity[i]["sign"] == '-' and monotonicity[i+1]["sign"] == '+':
        cp = critical_point[i+1]
        local_extrema.append({
            "x=": cp,
            "f(x) attains": "local minimum",
            "value": float(f.subs(x, cp)),
        })
sleep()
print("\033[31mlocal extrema completed...\033[0m")
d2f = sp.diff(f, x, 2)

sleep()
print(f"f''={d2f.evalf()}")
sec_ord_pnt = sp.solve(sp.Eq(d2f, 0), x)

sec_ord_pnt.insert(0, float('-inf'))
sec_ord_pnt.append(float('inf'))

# -------------------------
# CONCAVITY
# -------------------------
for i in range(len(sec_ord_pnt) - 1):


    if len(sec_ord_pnt)-2==i:
        test_point=sec_ord_pnt[i]+1
    else:
        test_point=sec_ord_pnt[i+1]-1
    sub = d2f.subs(x, test_point)

    if sub.evalf() < 0:
        concavity.append({
            "limit": f"{sec_ord_pnt[i]}<x<{sec_ord_pnt[i+1]}",
            "sign": "-",
            "f(x) attains": "concave down",
            "x=": sec_ord_pnt[i],
            "start": sec_ord_pnt[i],
            "end": sec_ord_pnt[i+1]
        })
    else:
        concavity.append({

            "limit": f"{sec_ord_pnt[i]}<x<{sec_ord_pnt[i+1]}",
            "sign": "+",
            "f(x) attains": "concave up",
            "x=": sec_ord_pnt[i],
            "start": sec_ord_pnt[i],
            "end": sec_ord_pnt[i+1]
        })
sleep()
print("\033[31mconcavity  completed...\033[0m")
# -------------------------
# INFLECTION
# -------------------------
for i in range(len(concavity) - 1):
    if concavity[i]["end"] == concavity[i+1]["start"]:
        p = concavity[i]["end"]
        inflection.append({
            "x=": p,
            "value": f.subs(x, p)
        })
sleep()
print("\033[31minflection completed...\033[0m\n")
sleep()
print("\n\033[33mMonotonicity:\033[0m\n-------------------------------------")
for i in monotonicity:
    print(f"\033[34m{i}\033[0m")
print("-------------------------------------\n")
print("\033[33mLocal Extrema:\033[0m\n-------------------------------------")
for i in local_extrema:
    print(f"\033[34m{i}\033[0m")
print("-------------------------------------\n")
print("\033[33mConcavity:\033[0m\n-------------------------------------")
for i in concavity:
    print(f"\033[34m{i}\033[0m")
print("-------------------------------------\n")
print("\033[33mInflection Points:\033[0m\n-------------------------------------")
for i in inflection:
    print(f"\033[34m{i}\033[0m")
print("-------------------------------------\n")
####tabule form
data=[]
sleep()
print("\n\033[33mMonotonicity:\033[0m\n-------------------------------------")
if len(monotonicity)!=0:
    data.append(list((monotonicity[0].keys()))[0:4])
    for i in monotonicity:
        data.append(list(i.values())[0:4])
print(f"\033[34m{tabulate.tabulate(data[0:4],headers="firstrow",tablefmt="fancy_grid")}\033[0m")
print("-------------------------------------\n")
data.clear()
print("\033[33mLocal Extrema:\033[0m\n-------------------------------------")
if len(local_extrema)!=0:
    data.clear()
    data.append(list(local_extrema[0].keys()))
    for i in local_extrema:
        data.append(list(i.values()))
print(f"\033[34m{tabulate.tabulate(data,headers="firstrow",tablefmt="fancy_grid")}\033[0m")
print("-------------------------------------\n")
print("\033[33mConcavity:\033[0m\n-------------------------------------")
if len(concavity)!=0:
    data.clear()
    data.append(list(concavity[0].keys())[0:3])
    for i in concavity:
        data.append(list(i.values())[0:3])
print(f"\033[34m{tabulate.tabulate(data,headers="firstrow",tablefmt="fancy_grid")}\033[0m")
print("-------------------------------------\n")
print("\033[33mInflection Points:\033[0m\n-------------------------------------")
if len(inflection)!=0:
    data.clear()
    data.append(list(inflection[0].keys()))
    for i in inflection:
        data.append(list(i.values()))
print(f"\033[34m{tabulate.tabulate(data,headers="firstrow",tablefmt="fancy_grid")}\033[0m")
print("-------------------------------------\n")
def graph():
    global c_p,f;
    start=int(c_p[0])-10
    end=int(c_p[-1])+10
    step=0.1
    x_=start+step
    x_point=[x_]
    while x_<=end:
        x_+=step
        x_point.append(x_)
    y_point=[]
    for i in x_point:
        y_point.append(f.subs(x,i))
    plt.plot(x_point,y_point)

    ax=plt.gca()
    '''ax.spines["left"].set_position("center")
    ax.spines["bottom"].set_position("center")

    ax.spines["right"].set_position("center")
    ax.spines["top"].set_position("center")'''
    plt.xlabel("x")
    plt.ylabel("y")
    #plt.xticks(range(start,end,1))
    #plt.yticks(range(int(y_point[0]),int(y_point[-1]),1))
    plt.show()
graph()