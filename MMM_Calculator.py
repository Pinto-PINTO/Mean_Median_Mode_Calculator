# This is a calculator for Mean, Median and Mode of a data set.
# Enter -1 to to exit from entering a number
# Created ny Pinto https://github.com/Pinto-PINTO


def mean_median_mode_calculator():
    
    # Intitializing Variables #
    inputArray = []
    uniqueArray = []
    countArray = []
    max_vals_array = []
    out_of_loop = -1    
    num = 0
    totalOfArray = 0
    mean = 0
    median_formulae = 0
    median_locator = 0
    median = 0
    count = 0
    maximum = 0

    
    # User Input #  
    
    print("-------------------------------------")
    print("-------------------------------------")
    print("Mean Median Mode Calculator by PINTO")
    print("-------------------------------------")
    print("-------------------------------------")
    print("Enter numbers one by one ...")
    print("To exit, enter -1")
    print("-------------------------------------")
          
    while num != out_of_loop:
        num = int(input("Enter number : "))
        inputArray.append(num)
             
    inputArray.remove(out_of_loop)   # removes the condition checking integer -1     
    inputArray.sort()
    
          
    
    
    # Calculating Mean #
    
    for value in inputArray:
        totalOfArray = totalOfArray + value
     
    mean = totalOfArray / len(inputArray)
    
    
     
    
    # Calculating Median (Q2) #   
    
    median_formulae = 0.5 * (len(inputArray) + 1)     # calculates median from formulae
    
    median_locator = round(median_formulae) - 1       # find the exact location in the array
    
    median = inputArray[median_locator]
    
    
    
    
    # Calculating Mode #
    
    uniqueValues = set(inputArray)   # Gets all unique values from inputArray into a list
    
    for num in uniqueValues:
        uniqueArray.append(num)   # puts the values from list into an array
    
  
    # Finds the count of each element in the unique array respective to their indexes in a new array -> countArray
    for x in range(0, len(uniqueArray), 1):
        
        for y in range(0, len(inputArray), 1):
            if uniqueArray[x] == inputArray[y]:
                count = count + 1

        countArray.append(count) 
        count = 0   # re-initializing count to 0
    

    # Finding all occurances of the maximum value in the count array         
    
    maximum = max(countArray)   # returns the maximum in countArray
    
    max_vals_array = [i for i, val in enumerate (countArray) if val == maximum]  # iterates through countArray to display all occurances of the maximim
    

    
    
    # Display #
    
    print("-------------------------------------")
    print("Sorted Array : " + str(inputArray))
    print("No of elements : " + str(len(inputArray)))
    print("-------------------------------------")  
    print("-------------------------------------")
    print("Mean = " + str(mean))
    print("-------------------------------------")
    print("Median = " + str(median))
    
    if maximum == 1:
        print("-------------------------------------")  
        print("There is no mode")
        print("-------------------------------------")
    
    if maximum > 1:
        print("-------------------------------------") 
        for a in range(0, len(max_vals_array), 1):   
            print("Mode = " + str(uniqueArray[max_vals_array[a]]))      
        print("-------------------------------------") 
    

mean_median_mode_calculator()
