
print("Input number of frames: ", end="")
num_frames = int(input())


frames, page_faults, current_index, page_fault_flag = [], 0, 0, 'No'


print("Enter the page reference string (separated by space): ", end="")
ref_string = list(map(int, input().strip().split()))


print("\nRef Str|Frames →\t", end='')
for j in range(num_frames):
    print(j, end=' ')
print("Page Fault\n   ↓\n")


for page in ref_string:
    if page not in frames:
        
        if len(frames) < num_frames:
            frames.append(page)
        else:
            frames[current_index] = page
            current_index = (current_index + 1) % num_frames
        page_faults += 1
        page_fault_flag = 'Yes'
    else:
        page_fault_flag = 'No'

    
    print("   %d\t\t" % page, end='')
    for frame in frames:
        print(frame, end=' ')
    for _ in range(num_frames - len(frames)):
        print(' ', end=' ')
    print(" %s" % page_fault_flag)


total_requests = len(ref_string)
fault_rate = (page_faults / total_requests) * 100
print(f"\nTotal Page Requests: {total_requests}\nTotal Page Faults: {page_faults}\nFault Rate: {fault_rate:.2f}%")
