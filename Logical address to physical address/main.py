import p1
import p2

physicalMem = {}
translationLB = []
pageDirectory = []
faultCount = 0
tlbHits = 0
processedAddresses = 0

def main():
    global faultCount, tlbHits, processedAddresses
    output_file = open('Logical address to physical address/outputaddresses.txt', 'w')

    with open('Logical address to physical address/inputaddresses.txt', 'r') as inputFile:
        for addressLine in inputFile:
            isTLBHit = 0
            pageTableFound = 0

            logicalAddr = int(addressLine)
            offsetValue = logicalAddr & 255
            pageOriginalValue = logicalAddr & 65280
            pageNum = pageOriginalValue >> 8
            processedAddresses += 1

            isTLBHit = p1.tlbLookup(pageNum, physicalMem, offsetValue, logicalAddr, translationLB, processedAddresses, output_file)

            if isTLBHit != 1:
                pageTableFound = p1.pageTableLookup(pageNum, logicalAddr, offsetValue, processedAddresses, pageDirectory, physicalMem, output_file)

                if pageTableFound != 1:
                    print("Handling page fault for Page Number: " + str(pageNum))
                    p2.handlePageFault(pageNum, translationLB, pageDirectory, physicalMem)
                    faultCount += 1
                    
                    p1.tlbLookup(pageNum, physicalMem, offsetValue, logicalAddr, translationLB, processedAddresses, output_file)

    
    faultRate = faultCount / processedAddresses
    hitRateTLB = tlbHits / processedAddresses
    resultStr = 'Total Addresses Processed: ' + str(processedAddresses) + '\n' + \
                'Total Page Faults: ' + str(faultCount) + '\n' + \
                'Page Fault Rate: ' + "{:.2f}".format(faultRate) + '\n' + \
                'Total TLB Hits: ' + str(tlbHits) + '\n' + \
                'TLB Hit Rate: ' + "{:.2f}".format(hitRateTLB) + '\n'

    print(resultStr)
    output_file.write(resultStr)
    print("Physical Memory Snapshot: ", physicalMem)
    print("TLB Snapshot: ", translationLB)
    print("Page Table Snapshot: ", pageDirectory)

    output_file.close()

if __name__ == '__main__':
    main()
