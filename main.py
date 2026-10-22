# sample data
data = [2, 8, 10, 10, 12, 13, 15, 16, 17, 19, 22, 43]

# calculate the mean 
sum = 0
length = len(data)
for i in range (length):
    sum = sum + data[i]

mean_value = sum / length
print("For the data ", data , "the mean is" , mean_value)


# calculate median
if (length % 2 == 0):
    median_value = (data[int(length/2 - 1)] + data[int(length/2)])/2
else:
    median_value = data[int(length/2)]

print("The median of the data", data, " is ", median_value)
