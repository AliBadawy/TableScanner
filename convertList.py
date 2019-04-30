
y = [ "hello" , "27.2" , "Ahmed" , "24.1"]

def List2Dict(listOfData, NoOfCol, NoOfRow):
    output = {}
    output['column'] = NoOfCol
    output['rows'] = NoOfRow
    counter = 0
    for r in range(NoOfRow):
        temp = {}
        for c in range(NoOfCol):
              # output['rowsdata']
              temp['col'+str(c+1)] = listOfData[counter]
              # print(listOfData[counter])
              counter += 1
              output['rowsdata'] = temp
    return output



print(List2Dict(y,2,2))