import random
import time
import math

def OneDieS(trials, sides):
    c1=time.clock()
    print("====================")
    print("Number of sides = ", sides)
    print("Number of trials = ", trials)

    histogram = []
    for s in range(sides):
        histogram.append(0)
    print(histogram)

    r = 0
    sum1 = 0
    sum2 = 0
    for t in range(trials):
        r = int(random.random()*sides)
        histogram[r] = histogram[r] + 1
        sum1 = sum1 + (r+1)
        sum2 = sum2 + (r+1)**2
    mean = sum1/trials
    variance = sum2/trials - mean**2
    std_dev = math.sqrt(variance)
    
    print( histogram)
    
    theo_mean = (sides+1)/2
    sum3 = 0
    
    for s in range(sides):
        sum3 = sum3 + (1/sides)*((s+1)**2)
    
        
    #print(sum3)
    theo_var = sum3 - theo_mean**2
    theo_std_dev = math.sqrt(theo_var)
    error1 = abs(mean - theo_mean)/theo_mean
    error2 = abs(std_dev - theo_std_dev)/theo_std_dev
    print("sides=", sides, "mean=", mean, "variance=", variance, "std_dev=", std_dev, "theo_mean=", theo_mean, "theo_var=", theo_var, "theo_std_dev", theo_std_dev, "error_mean=", error1, "error_std_dev=", error2)
    

    c2=time.clock()
    print("Elapsed time =", c2-c1)
    

def trial_number_mean(sides):
    global trial1
    theor_mean = (sides+1)/2
    sum3 = 0
    for i in range(sides):
        sum3 = sum3 + (1/sides)*((i+1)**2)
    
    theo_var = sum3 - theor_mean**2
    theo_std_dev = math.sqrt(theo_var)
    
    trial1 = 1
    
    
    delta_mean = 1
    while delta_mean >= 0.01:
        sum4 = 0
        sum5 = 0
        for j in range(trial1):
            #print("trial1=", trial1)
            rr = int(random.random()*sides)
            sum4 = sum4 + (rr+1)
            sum5 = sum5 + (rr+1)**2
        #print("sum4=",sum4)
        mean = sum4/trial1
        #print(mean)
        variance = sum5 - mean**2
        std_dev = math.sqrt(variance)
        delta_mean = abs(mean - theor_mean)/theor_mean
        #print("mean - theor_mean=", mean - theor_mean)
        #print("theor_mean=", theor_mean)
        trial1 = trial1 + 1
        #print("trial1=", trial1)
        
        
    print("trial1=", trial1)
    

def trial_number_std_dev(sides):
    global trial2
    
    theor_mean = (sides+1)/2
    sum3 = 0
    for i in range(sides):
        sum3 = sum3 + (1/sides)*((i+1)**2)
    #print(sum3)
    theo_var = sum3 - theor_mean**2
    theo_std_dev = math.sqrt(theo_var)
    
    trial2 = 1
    
    delta_std_dev = 1
    while delta_std_dev >= 0.01:
        sum4 = 0
        sum5 = 0
        for j in range(trial2):
            rr = int(random.random()*sides)
            sum4 = sum4 + (rr+1)
            sum5 = sum5 + (rr+1)**2
        mean = sum4/trial2
        variance = sum5/trial2 - mean**2
        std_dev = math.sqrt(variance)
        delta_std_dev = abs(std_dev - theo_std_dev)/theo_std_dev
        #print(delta_std_dev)
        trial2 = trial2 + 1
    print("trial2=", trial2)


          

def run1():
    OneDieS(1, 8)
    OneDieS(10, 8)
    OneDieS(100, 8)
    OneDieS(1000, 8)
    OneDieS(5000, 8)
    OneDieS(10000, 8)
    OneDieS(100000, 8)
    OneDieS(1000000, 8)


def run2():
    print("different trials")
    OneDieS(100000, 4)
    OneDieS(1000000, 4)


def run3():
    print("different side")
    OneDieS(100000, 5)
    OneDieS(100000, 7)


def run4():
    trial_number_mean(15)


def run5():
    trial_number_std_dev(15)
    
    

    
    
run1()
run2()
run3()
run4()
run5()
