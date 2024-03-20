print("Input total frame count: ", end="")
frame_count = int(input())


frames, usage_stack, page_fault_count, is_page_fault = [], [], 0, 'No'


print("Enter page reference string (space-separated): ", end="")
reference_string = list(map(int, input().strip().split()))


print("\nRef|Frames →\t", end='')
for frame_index in range(frame_count):
    print(frame_index, end=' ')
print("Fault\n   ↓\n")


for page in reference_string:
    if page not in frames:
       
        if len(frames) < frame_count:
            frames.append(page)
            usage_stack.append(len(frames) - 1)
        else:
            least_recent_index = usage_stack.pop(0)
            frames[least_recent_index] = page
            usage_stack.append(least_recent_index)
        is_page_fault = 'Yes'
        page_fault_count += 1
    else:
        
        usage_stack.append(usage_stack.pop(usage_stack.index(frames.index(page))))
        is_page_fault = 'No'

    
    print("   %d\t\t" % page, end='')
    for frame in frames:
        print(frame, end=' ')
    for _ in range(frame_count - len(frames)):
        print(' ', end=' ')
    print(" %s" % is_page_fault)


total_page_requests = len(reference_string)
fault_rate = (page_fault_count / total_page_requests) * 100
print(f"\nTotal Page Requests: {total_page_requests}\nTotal Page Faults: {page_fault_count}\nFault Rate: {fault_rate:.2f}%")
