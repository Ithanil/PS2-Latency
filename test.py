from pylab import *


# load data from files and create dictionary

llmoff_maxfps = genfromtxt('LLMOFF_MaxFPS_at300')
llmoff_nolimit = genfromtxt('LLMOFF_NoLimit_about340FPS')
llmoff_nvfps = genfromtxt('LLMOFF_NVFPS_at300')
llmoff_smoothing = genfromtxt('LLMOFF_Smoothing_at300')
llmon_maxfps = genfromtxt('LLMON_MaxFPS_at300')
llmon_nolimit_1 = genfromtxt('LLMON_NoLimit_about335FPS')
llmon_nolimit_2 = genfromtxt('LLMON_NoLimit_about335FPS_Run2')
llmon_nvfps = genfromtxt('LLMON_NVFPS_at300')
llmon_smoothing = genfromtxt('LLMON_Smoothing_at300')
null_maxfps = genfromtxt('NULL_MaxFPS_at300')
null_nolimit_1 = genfromtxt('NULL_NoLimit_about330FPS')
null_nolimit_2 = genfromtxt('NULL_NoLimit_about330FPS_Run2')
null_nvfps = genfromtxt('NULL_NVFPS_at300')
null_smoothing = genfromtxt('NULL_Smoothing_at300')

llmon_nolimit = concatenate((llmon_nolimit_1, llmon_nolimit_2))
null_nolimit = concatenate((null_nolimit_1, null_nolimit_2))

data = {('llmoff', 'maxfps') : llmoff_maxfps,
        ('llmoff', 'nolimit') : llmoff_nolimit,
        ('llmoff', 'nvfps') : llmoff_nvfps,
        ('llmoff', 'smoothing') : llmoff_smoothing,
        ('llmon', 'maxfps'): llmon_maxfps,
        ('llmon', 'nolimit') : llmon_nolimit,
        ('llmon', 'nvfps') : llmon_nvfps,
        ('llmon', 'smoothing') : llmon_smoothing,
        ('null', 'maxfps') : null_maxfps,
        ('null', 'nolimit') : null_nolimit,
        ('null', 'nvfps') : null_nvfps,
        ('null', 'smoothing') : null_smoothing}


# process and sort data

mean_x = []
mean_y = []
std_y = []
min_y = []
max_y = []
all_y = []
for key in data.keys():
    print(key, mean(data[key]), std(data[key]), min(data[key]), max(data[key]))
    mean_x.append(str(key))
    mean_y.append(mean(data[key]))
    std_y.append(std(data[key]))
    min_y.append(min(data[key]))
    max_y.append(max(data[key]))
    all_y.append(data[key])

yx = sorted(zip(mean_y, mean_x), reverse = True)
yy_std = sorted(zip(mean_y, std_y), reverse = True)
yy_min = sorted(zip(mean_y, min_y), reverse = True)
yy_max = sorted(zip(mean_y, max_y), reverse = True)
ya = sorted(zip(mean_y, all_y), reverse = True)
mean_x = [x for y, x in yx]
mean_y = [y for y, x in yx]
std_y = [y1 for y2, y1 in yy_std]
min_y = [y1 for y2, y1 in yy_min]
max_y = [y1 for y2, y1 in yy_max]
all_y = [a for y, a in ya]


# Comparing Test 1 and 2 for LLM_ON/NoLimit and NULL/NoLimit

print('LLM_ON/NoLimit Test, Retest')
print(mean(llmon_nolimit_1), std(llmon_nolimit_1))
print(mean(llmon_nolimit_2), std(llmon_nolimit_2))

print('NULL/NoLimit Test, Retest')
print(mean(null_nolimit_1), std(null_nolimit_1))
print(mean(null_nolimit_2), std(null_nolimit_2))


# Plot

figure()
barh(mean_x, mean_y, xerr = std_y)

fig, ax = subplots()
ylen = len(mean_y)
for it, y in enumerate(mean_y):
    ax.axvspan(min_y[it], max_y[it], (it + 0.25)/ylen, (it + 0.75)/ylen, color = 'blue')
    ax.axvspan(y - std_y[it], y + std_y[it], (it + 0.25)/ylen, (it + 0.75)/ylen, color = 'red')
    ax.axvspan(y - std_y[it]/sqrt(len(all_y[it])), y + std_y[it]/sqrt(len(all_y[it])), (it + 0.25)/ylen, (it + 0.75)/ylen, color = 'black')
ax.set_yticks(arange(0.5, len(mean_y) + 0.5) / ylen)
ax.set_yticklabels(mean_x)

show()
