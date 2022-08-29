import matplotlib.pyplot as plt
import time


def f(num, steps=0):
    if num == 4:
        values.append(2)
        values.append(1)
    else:
        if num % 2 == 0:
            num = num//2
        else:
            num *= 3
            num += 1

        values.append(num)
        steps += 1
        f(num, steps)  # recursion


n1 = int(input("Enter num for algorithm '3x+1' from "))
n2 = int(input("to:"))
start = time.time()
delta = n2 - n1
onepercent = delta / 100
fig, ax = plt.subplots()
ax.set(xlabel='steps', ylabel='values',
       title=f'3x+1 algorithm for numbers from {n1} to {n2}')
ax.grid()
print("Calculating values... 0%", end="")
percents = 0
time_remain = ""
start2 = time.time()
for i in range(n1, n2):
    values = [i]
    f(i)
    # data for plotting
    x = [j for j in range(len(values))]
    y = values
    plt.plot(x, y, label=f"line <{i}>",linewidth=0.5)
    count = i-n1
    if count//onepercent != percents:
        if percents != 0:
            onepercenttimepass = (time.time() - start2) / percents
            time_remain = onepercenttimepass*(100-percents)
            time_remain = round(time_remain, 3)
        percents = count//onepercent
        print("\rCalculating values...", percents, "%",
              "about", time_remain, "seconds remain", end="")
print("\nCalculating values... 100 %")
print("All values were calculated at", time.time()-start2)
print(" Saving plot - pic.png ...")
start3 = time.time()
fig.savefig("pic.png",dpi=1000)
print("Plot was saved at", time.time()-start3)
end = time.time()

print(f"Program finished at {end-start} seconds.")
