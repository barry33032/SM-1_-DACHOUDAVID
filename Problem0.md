# Problem 0
1. code (have also hand in .py file)<br />
    import random<br />
    import time<br />

    def OneDie(trials):<br />
        c1=time.clock()<br />
        print("="*30)<br />
        print("One die with 6 sides")<br />
        print("Number of trials = ", trials)<br />

        sides = 6<br />
        theo_histogram_occur_times = [0, 0, 0, 0, 0, 0]<br />
        theo_histogram_frequency= [0, 0, 0, 0, 0, 0]<br />
        histogram_occur_times = [0, 0, 0, 0, 0, 0]<br />
        histogram_frequency= [0, 0, 0, 0, 0, 0]<br />
        print(histogram_occur_times)<br />
        print(histogram_frequency)<br />

        j = 0<br />
        r = 0<br />
        while j < trials :<br />
            r = int(random.random()*sides) # Faster<br />
            histogram_occur_times[r] = histogram_occur_times[r] + 1<br />
            j = j + 1<br />
        
        print("histogram_occur_times=",histogram_occur_times)<br />
        histogram_frequency = [histogram_occur_times[i]/trials for i in range(sides)]<br />
        print("histogram_frequency=",histogram_frequency)<br />

        for i in range(sides):<br />
            theo_histogram_occur_times[i] = (1/6)*trials<br />
            theo_histogram_frequency[i] = 1/6<br />
            print(i+1, "theo_histogram_occur_times=",theo_histogram_occur_times[i], "theo_histogram_frequency=",theo_histogram_frequency[i])<br />
            print(i+1, "difference=",histogram_occur_times[i]-theo_histogram_occur_times[i])<br />
            print(i+1, "ratio=",histogram_occur_times[i]/trials, "ratio difference=",histogram_occur_times[i]/trials- (1/6))<br />
        
        c2=time.clock()<br />
        print("Elapsed time =", c2-c1)<br />


    OneDie(10)<br />
    OneDie(100)<br />
    OneDie(1000)<br />
    OneDie(10000)<br />
    OneDie(100000)<br />
    OneDie(1000000)<br />
    
2. One die with 6 sides<br />
Number of trials =  100<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [15, 12, 21, 20, 17, 15]<br />
histogram_frequency= [0.15, 0.12, 0.21, 0.2, 0.17, 0.15]<br />

3. One die with 6 sides<br />
Number of trials =  10<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [2, 0, 2, 4, 2, 0]<br />
histogram_frequency= [0.2, 0.0, 0.2, 0.4, 0.2, 0.0]<br />
<br />
One die with 6 sides<br />
Number of trials =  100<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [15, 12, 21, 20, 17, 15]<br />
histogram_frequency= [0.15, 0.12, 0.21, 0.2, 0.17, 0.15]<br />
<br />
One die with 6 sides<br />
Number of trials =  1000<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [167, 175, 187, 163, 155, 153]<br />
histogram_frequency= [0.167, 0.175, 0.187, 0.163, 0.155, 0.153]<br />
<br />
One die with 6 sides<br />
Number of trials =  10000<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [1633, 1688, 1668, 1654, 1739, 1618]<br />
histogram_frequency= [0.1633, 0.1688, 0.1668, 0.1654, 0.1739, 0.1618]<br />
<br />
One die with 6 sides<br />
Number of trials =  100000<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [16727, 16638, 16501, 16678, 16721, 16735]<br />
histogram_frequency= [0.16727, 0.16638, 0.16501, 0.16678, 0.16721, 0.16735]<br />
<br />
One die with 6 sides<br />
Number of trials =  1000000<br />
[0, 0, 0, 0, 0, 0]<br />
[0, 0, 0, 0, 0, 0]<br />
histogram_occur_times= [166512, 166901, 166049, 166462, 166973, 167103]<br />
histogram_frequency= [0.166512, 0.166901, 0.166049, 0.166462, 0.166973, 0.167103]<br />

4. As the number of trials increases, does the magnitude (absolute value) of the differences between the number of times a given side occurs and one-sixth of the number of trials may increase or decrease.

5. As increasing the number of trials, the ratio of the number of times each side occurs to the total number of trials approach closer to 1/6.


# Problem 1
1. The theoretical values of the mean: (sides+1)/2<br />
variance: (sum all sides of (1/sides)*((s+1)^2))-theo_mean^2<br />
standard deviation:(variance)^0.5<br />
2. Number of sides =  8<br />
Number of trials =  100<br />
[0, 0, 0, 0, 0, 0, 0, 0]<br />
[15, 12, 8, 13, 14, 12, 14, 12]<br />
sides= 8 mean= 4.51 variance= 2558.6599 std_dev= 50.58319780322316 theo_mean= 4.5 theo_var= 5.25 theo_std_dev 2.29128784747792<br />
3. Number of sides =  5<br />
Number of trials =  100000<br />
mean= 3.00189<br /> variance= 2.003326427900001<br /> std_dev= 1.4153891436279993<br /> theo_mean= 3.0<br /> theo_var= 2.0<br /> theo_std_dev 1.4142135623730951<br />
===============================================================<br />
Number of sides =  7<br />
Number of trials =  100000<br />
mean= 3.99851<br /> variance= 4.0006077798999975<br /> std_dev= 2.000151939203619<br /> theo_mean= 4.0<br /> theo_var= 4.0<br /> theo_std_dev 2.0<br />
The results are familiar with prediction<br />
4. Different trials for mean and standard deviation<br />
mean:45<br />
standard deviation:25<br />


