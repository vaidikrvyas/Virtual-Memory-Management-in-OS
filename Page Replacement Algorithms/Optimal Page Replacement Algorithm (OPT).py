print("Number of frames: ", end="")
num_frames = int(input())


frames, total_faults, has_fault = [], 0, 'No'


print("Reference string (separated by space): ", end="")
ref_string = list(map(int, input().strip().split()))

print("\nRef Str|Frames →\t", end='')
for frame in range(num_frames):
    print(frame, end=' ')
print("Fault\n   ↓\n")


next_occurrence = [None for _ in range(num_frames)]


for index, page in enumerate(ref_string):
    if page not in frames:
        if len(frames) < num_frames:
            frames.append(page)
        else:
            for frame_index in range(len(frames)):
                if frames[frame_index] not in ref_string[index + 1:]:
                    frames[frame_index] = page
                    break
                else:
                    next_occurrence[frame_index] = ref_string[index + 1:].index(frames[frame_index])
            else:
                max_index = next_occurrence.index(max(next_occurrence))
                frames[max_index] = page
        total_faults += 1
        has_fault = 'Yes'
    else:
        has_fault = 'No'


    print("   %d\t\t" % page, end='')
    for frame_val in frames:
        print(frame_val, end=' ')
    for _ in range(num_frames - len(frames)):
        print(' ', end=' ')
    print(" %s" % has_fault)


fault_rate = (total_faults / len(ref_string)) * 100
print(f"\nTotal Page Requests: {len(ref_string)}\nTotal Page Faults: {total_faults}\nFault Rate: {fault_rate:.2f}%")
