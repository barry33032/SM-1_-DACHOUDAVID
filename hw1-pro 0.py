import random
import time

def OneDie(trials):
    c1=time.clock()
    print("="*30)
    print("One die with 6 sides")
    print("Number of trials = ", trials)

    sides = 6
    theo_histogram_occur_times = [0, 0, 0, 0, 0, 0]
    theo_histogram_frequency= [0, 0, 0, 0, 0, 0]
    histogram_occur_times = [0, 0, 0, 0, 0, 0]
    histogram_frequency= [0, 0, 0, 0, 0, 0]
    print(histogram_occur_times)
    print(histogram_frequency)

    j = 0
    r = 0
    while j < trials :
        r = int(random.random()*sides) # Faster
#         r = random.randint(0,5) # Slower. Return random integer in range [a, b], including both end points.
        histogram_occur_times[r] = histogram_occur_times[r] + 1
        j = j + 1
        
    print("histogram_occur_times=",histogram_occur_times)
    histogram_frequency = [histogram_occur_times[i]/trials for i in range(sides)]
    print("histogram_frequency=",histogram_frequency)

    for i in range(sides):
        theo_histogram_occur_times[i] = (1/6)*trials
        theo_histogram_frequency[i] = 1/6
        print(i+1, "theo_histogram_occur_times=",theo_histogram_occur_times[i], "theo_histogram_frequency=",theo_histogram_frequency[i])
        print(i+1, "difference=",histogram_occur_times[i]-theo_histogram_occur_times[i])
        print(i+1, "ratio=",histogram_occur_times[i]/trials, "ratio difference=",histogram_occur_times[i]/trials- (1/6))
        
    c2=time.clock()
    print("Elapsed time =", c2-c1)


OneDie(10)
OneDie(100)
OneDie(1000)
OneDie(10000)
OneDie(100000)
OneDie(1000000)
    
    

