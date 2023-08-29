import statistics as stats

data_A = [10, 11, 14, 20, 20 , 20, 22, 24, 28, 31]

mean_A = stats.mean(data_A)
median_A = stats.median(data_A)
mode_A = stats.mode(data_A)
variance_A = stats.pvariance(data_A)
                    
print("Mean of Data A = " , mean_A)
print("Median of Data A = " , median_A)
print("Mode of Data A = " , mode_A)
print("Variance of Data A = ", variance_A)

data_B = [2,9, 13, 14, 20, 20 ,24, 26, 32, 40]

mean_B = stats.mean(data_B)
median_B = stats.median(data_B)
mode_B = stats.mode(data_B)
variance_B = stats.pvariance(data_B)

print ("Mean of  Data B = ", mean_B)
print("Median of Data B = " , median_B)
print("Mode of Data B = " , mode_B)
print("Vraince of Data B " , variance_B)