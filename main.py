import csv

#file paths for our in and out files
in_csv = './in.csv'
out_csv ='./out.csv'

#our data structure for pre-process data
in_data = []

#our data stucture for holding post processed data
out_data = []

#this opens the in csv
with open(in_csv) as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        in_data.append(row)

for i in range(0, len(in_data)):
    #this puts the column titles on our out document
    if i ==0:
        out_data.append(in_data[i])
    
    #this builds the row for our out data
    if i > 0:
        lcl_row = in_data[i]
        local_val = lcl_row[1]
        one = i+1
        print

        two = i+2
        r_zero = in_data[i][1]

        #the below try catches handle the end of list 
        try:
            r_one = in_data[one][1]
        except IndexError:
            r_one = ''
        try:
            r_two = in_data[two][1]
        except IndexError:
            r_two =''
        # print("current row: {}".format(lcl_row))
        # print("next row: {}".format(r_one))
        # print("second row: {}".format(r_two))
        # print() 

        #here we make the new value
        new_val = local_val+r_one+r_two.strip(" ")
        # print(new_val)

        #here we make new row  with the new value 
        new_row = []
        new_row.append(i)
        new_row.append(local_val)
        new_row.append(new_val)

        #here we put that row on our out data
        out_data.append(new_row)

        # print()


#saves our post processed data to a csv
with open(out_csv, mode='w') as out:
    writer = csv.writer(out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for d in out_data:
        writer.writerow(d)