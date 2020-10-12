# # Importing libraries to deal with data sets
import pandas as pd
import pandas_profiling as pp
df = pd.read_csv("webdevelopers.csv")
# ------------------------------------------------------ #
# # Exploratory Data Analysis using pandas_profiling
profile = pp.ProfileReport(df)
# profile.to_file("Report.html")
print(df.dtypes)
# ----------------------------------------------------- #
# Extracting the columns of interest
new_df = df[["rates","skill1","skill2","skill3","skill4","skill5","nrOfPortfolio"]]
print(new_df.shape)
profile = pp.ProfileReport(new_df)
# profile.to_file("Report1.html")
# ------------------------------------------------------ #
# Analysing the rates_distribution of freelancers
List1 = list(new_df.rates)
List1_modified = []
import re
for i in range(len(List1)):
    x = List1[i]
    y = x[1:3]
    z = re.sub(r'[^\w]','', y)
    w = int(z)
    List1_modified.append(w)
List1_modified.remove(44)
Count = len(List1_modified)
Sum = sum(List1_modified)
mean = Sum/Count
print(Count,Sum,mean)
Min = min(List1_modified)
Max = max(List1_modified)
print(Min,Max)
Lm_unique = set(List1_modified)
Lm_unique_list = list(Lm_unique)
Lm_unique_count = []
for i in Lm_unique:
    occurences = List1_modified.count(i)
    Lm_unique_count.append(occurences)
print(Lm_unique_count)
#from matplotlib import pyplot as plt
#plt.title("Earnings for Web development")
#plt.bar(Lm_unique_list,Lm_unique_count,color = "red")
#plt.show()
Sum1 = sum(Lm_unique_count)
Percentage = []
for i in Lm_unique_count:
    percent = (i/Sum1)*100
    Percentage.append(round(percent))
print(Percentage)
df_count = pd.DataFrame(list(zip(Lm_unique_list,Percentage)),
                        columns=["rates","percentage"])
print(df_count)
print("Minimum earning is $"+str(Min)+"/hour")
print("Maximum earning is $"+str(Max)+"/hour")
mp_index = Percentage.index(max(Percentage))
value = Lm_unique_list[mp_index]
print(str(max(Percentage)) + "% of Freelancers earn "+ "$"+str(value)+" /hour")
from matplotlib import pyplot as plt
plt.title("Earnings for Web development")
plt.xlabel("Amount in dollars $")
plt.ylabel("Percentage of Freelancers")
plt.bar(Lm_unique_list,Percentage,color = "red")
# plt.show()

## Skill 2
List2 = list(new_df.skill2)
##Skill 3
List3 = list(new_df.skill3)
## Skill 4
List4 = list(new_df.skill4)
## Skill 5
List5 = list(new_df.skill5)
End_list = List2+List3+List4+List5
unique_list = set(End_list)
print(len(End_list))
wordfreq = []
for w in unique_list:
    wordfreq.append(End_list.count(w))
print("Pairs 5\n" + str(list(zip(unique_list,wordfreq))))
Listfinal = list(zip(unique_list,wordfreq))
for i in range(len(Listfinal)):
    print(Listfinal[i])
import numpy as np
ztt = []
for i in End_list:
    if i!='np.nan':
        ztt.append(i)
print(len(ztt))
#df_wc2 = pd.DataFrame(Listfinal,columns=["word","freq"])
#df_wc2.to_csv("Wordclouddata2.csv")
#convert it to dictionary with values and its occurences
dfwcf = pd.read_csv("Wordclouddata.csv")
profile = pp.ProfileReport(dfwcf)
profile.to_file("report3.html")







