import numpy as np
import matplotlib.pyplot as plt
import random
import seaborn as sns

iterationAmount = 10000
dicethrowAmount = 2
diceside = 12
throwMin = 2
throwMax = 8
number_of_colors = 10

color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(throwMax-throwMin)])
             for i in range(number_of_colors)]

def RollDice(diceSide,iterationNum,dtamount):

    all_results = np.zeros((iterationNum,dtamount))

    for i in range(iterationNum):
        for j in range (dtamount):
            all_results[i,j] = random.randint(1,diceSide)

    print("------ALL RESULTS------")
    print(all_results)

    probability = np.zeros(iterationNum)
    probability_count = [np.arange(0,dtamount),np.zeros(dtamount)]
    print(probability_count[0])

    # Check the dice results, probability and number of sames
    for i in range(iterationNum):
           index = 0
           checkedDiceNum = np.zeros((2, dtamount))

           for j in range(dtamount):
               #Dice Results
               if (all_results[i, j] not in checkedDiceNum[0,:]):
                   #Check how many of them are similar
                   for k in range(j + 1, dtamount):
                       if (all_results[i, j] == all_results[i, k]):
                           checkedDiceNum[0, index] = all_results[i, k]
                           checkedDiceNum[1, np.where(checkedDiceNum[0, :] == all_results[i, k])] += 1
               index += 1
           #Add the maximums for showing in graph
           probability[i] = checkedDiceNum[1, :].max()

           #Check amount of probability nums in each iteration
           for k in range(dtamount):
              if(probability[i] == probability_count[0][k]):
                  probability_count[1][k] += 1


    print(probability_count)
    #Return different arrays for diferent calculations
    return all_results,np.int_(probability),probability_count

#For calculating linear regression
def LinRegres(valuesX,valuesY):

    linRegY = np.array([value - np.mean(valuesY) for value in valuesY])
    linRegX = np.array([value - np.mean(valuesX) for value in valuesX])

    slope = np.sum(np.multiply(linRegX,linRegY))/np.sum(np.power(linRegX,2))

    constant_val = np.mean(valuesY) - slope * np.mean(valuesX)

    equation = f"Liner Regression Equation: y = {str(round(constant_val,4))} + {slope}x"
    return (constant_val + (slope)*valuesX) , equation

xAxis = np.arange(iterationAmount)

plt.style.use('seaborn')
sns.set_style("darkgrid")

fig = plt.figure(constrained_layout=True)
subfigs = fig.subfigures(1, 2, wspace=0.07, width_ratios=[1., 1.])

ax1 = subfigs[0].subplots(1,1)
ax2 = subfigs[1].subplots(throwMax-throwMin,1)

subfigs[0].supxlabel("Number of Tries")
subfigs[0].supylabel("Probability Factor")

strlabel = ""

for x in range(throwMin,throwMax):

    #Setup parameters for each iteration
    yAxis = RollDice(diceside, iterationAmount, x)
    subAx = ax2[x-throwMin]
    currentColor = color[x]

    infolabel = f"Throwing {diceside}-sided dice with {x} times at the same (Iteration: {iterationAmount})"

    sns.scatterplot(label = infolabel,x= xAxis,color = currentColor,y = yAxis[1],ax = ax1,alpha=0.5,s =random.randint(12,20))
    sns.lineplot(x = xAxis,y = LinRegres(xAxis,yAxis[1])[0],label = LinRegres(xAxis,yAxis[1])[1],color = currentColor,ax = ax1,linestyle = "--")
    ax1.legend(loc="upper right")

    xTicks = np.zeros(x,dtype="object")

   #For showing on legend table not x label. OPTIONAL
   # for y in range(0, x):
   #     strlabel += f"{yAxis[2][0][y] + 1}: {100 * yAxis[2][1][y] / iterationAmount}%\n"

    for y in range(0, x):
        xTicks[y]  =  f"{y} \n {100 * yAxis[2][1][y] / iterationAmount}%"


    sns.histplot(ax = subAx,color=currentColor,x=yAxis[1],alpha = 0.5,discrete=True,binwidth=0.5,kde=True)
    subAx.legend(loc="upper right")
    subAx.set_xticks(np.arange(x),xTicks)
    subAx.tick_params(axis='x', color = currentColor)
    subAx.set_title(f"{diceside}-sided {x} dice")
    subAx.set_xlabel("Probability Factor")
    subAx.set_ylabel("Number of Iterations")

    strlabel = ""

plt.show()
