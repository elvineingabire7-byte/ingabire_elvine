#Phone repair intake
#Integer values
#MArks for students in phone repair assignment
import array
marks=[70,89,90,68,98,65,87,67]
total_marks= sum(marks)
average_marks= total_marks/len(marks)
min_marks= min(marks)
max_marks= max(marks)
print("Student's marks:")
print("Total marks:", total_marks)
print("Average marks:", average_marks)
print("Minimum marks:", min_marks)
print("Maximum marks:", max_marks)
#string report
report = (
    f"Phone Repair Report:\n"
    f"Total repairs = {total_marks}, "
    f"Average repairs = {average_marks:.2f}\n"
)
report += f"Minimum = {min_marks}, Maximum = {max_marks}"
print("String Report:")
print(report)
#Boolean
threshold=20
if average_marks>threshold and max_marks>threshold:
    print("Above the standard")
else:
    print("Below the standard")
    print()
 #List
items_list=["Soldering Iron","Pry Tool","Voltage Tester Multimeter","The Anti-Static Strap","Screwdriver Kits",]
print("Item list",items_list)
items_list.append("Curved Tweezers")
items_list.remove("Pry Tool")
items_list.sort()
print("New list",items_list)
#Array
repairs_array=array.array('i',[68,98,65,87,67])
array_sum=sum(repairs_array)
print("Repairs array",repairs_array)
print("Repairs sum",array_sum)
print("comparison with the list",items_list)
#Dictionaries
repair_intake = [
    {"ID": 1, "Name": "John", "Value": 12},
    {"ID": 2, "Name": "Mary", "Value": 8},
    {"ID": 3, "Name": "Ali", "Value": 15},
]
print("Original Records:", repair_intake)
repair_intake[1]["Value"] = 10  
del repair_intake[0] 
total_value = sum(record["Value"] for record in repair_intake)
print("Updated Records:", repair_intake)
print("Total of Values:", total_value)

