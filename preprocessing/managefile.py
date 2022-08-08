with open('try/label.txt','r') as firstfile, open('try/data.txt','w') as secondfile:
    # i = 0
    write = 1
    
    
    for line in firstfile:

    # append content to second file
        if "area" in line:
            # print(line)
            continue       
        
        if write == 0 and "}," in line:
            write = 1
        
        if write == 1:
            if "]," in line:
                line = line.replace(",", "")
                write = 0
            secondfile.write(line)
    

        # i = i + 1
        # if i == 350:
        #     print(line)
        #     break