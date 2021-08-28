#Project 5 - File Matching
#Name: Michelle Tan
#Date: November 27, 2020
#Section: 01
#Instructor: Prof. Turner

class Entry():
    #Creates attributes and objects for the input file information
    def __init__(self,account_num,name,balance,phone,city):
       self.account_num=account_num
       self.name=name
       self.balance=balance
       self.phone=phone
       self.city=city

def read_file(fileName):
    #Opens file and appends file info into fileInfo (which is a list)
    openFile=open(fileName)
    fileInfo=[]
    for i in openFile:
      fileInfo.append(i.split())
    openFile.close()
    return fileInfo

def sort_file(fileInfo):
    #Sorts the list from the fileInfo list and returns the sorted list
    sFileInfo=fileInfo
    sFileInfo.sort()
    return sFileInfo

def sort_acc_nums(fileInfo):
    #Takes only the account numbers from the fileInfo list and puts them in sortNums
    #Sorts the account numbers and returns the newly sorted list
    sortNums=[]
    for i in range(len(fileInfo)):
        j=fileInfo[i][0]
        sortNums.append(int(j))
    sortNums.sort()
    return sortNums

def sort_old_master(sFileInfo):
    #Opens sorted_oldMaster.dat file and writes the file information from the original file but the account numbers are sorted and the transactions aren't added yet
    openedOldMaster = open('sorted_oldMaster.dat','w')
    for i in range(len(sFileInfo)):
        s='{:4}{:6}{:11}{:10}{:15}{:12}'.format(sFileInfo[i][0],sFileInfo[i][1],sFileInfo[i][2],sFileInfo[i][3],sFileInfo[i][4],sFileInfo[i][5])
        if i == 0:
           openedOldMaster.write(s)
        else:
           openedOldMaster.write('\n'+(s))
    openedOldMaster.close()

def transaction(sList,tFileInfo,accNums):
    #Computates the transactions and adds the initial amount to the added amount to form the new balance
    #Searches for unmatched transactions and those values are put into the unknownList   
    unknownList=[]
    for i in range(len(sList)):
        for j in range(len(tFileInfo)):
            try:
                if tFileInfo[j][0]==sList[i][0]:
                    sList[i][3]="{:.2f}".format(float(sList[i][3])+float(tFileInfo[j][1]))
                else:
                    if int(tFileInfo[j][0]) not in accNums:
                       accNums.append(int(tFileInfo[j][0]))
                       unknownList.append(int(tFileInfo[j][0]))
            except:
                pass
    newFileInfo=[unknownList,sList]
    return(newFileInfo)

def new_master(sFileInfo):
    #Opens the newMaster.dat file and writes the file information with the newly added transactions and lists the unmatched transactions
    openedNewMaster=open('newMaster.dat','w')
    for i in range(len(sFileInfo[1])):
        s='{:4}{:6}{:11}{:10}{:15}{:12}'.format(sFileInfo[1][i][0],sFileInfo[1][i][1],sFileInfo[1][i][2],sFileInfo[1][i][3],sFileInfo[1][i][4],sFileInfo[1][i][5])
        if i==0:
           openedNewMaster.write(s)
        else:
           openedNewMaster.write('\n'+(s))
    for j in range(len(sFileInfo[0])):
        openedNewMaster.write('\nUnmatched transaction record for account '+str(sFileInfo[0][j]))
    openedNewMaster.close()

def main():
    #Calls functions in order to create the newMaster file
    info=read_file('oldMaster.dat')
    sortInfo=sort_file(info)
    accNumList=sort_acc_nums(info)
    sort_old_master(sortInfo)
    transactionInfo=read_file('transaction.dat')
    sortInfo=transaction(sortInfo,transactionInfo,accNumList)
    new_master(sortInfo)

if __name__ == "__main__":
    main()
