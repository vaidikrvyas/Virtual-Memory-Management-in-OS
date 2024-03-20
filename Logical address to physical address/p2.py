def handlePageFault(page_num, trans_lb, page_dir, phys_mem):
    if page_num < 256:
        frame_num = next(i for i in range(256) if i not in phys_mem)
        with open("Logical address to physical address/BACKING_STORE.bin", "rb") as back_store:
            phys_mem[frame_num] = []
            for i in range(256):
                back_store.seek(page_num * 256 + i)
                data = str(int.from_bytes(back_store.read(1), byteorder='big', signed=True))
                phys_mem[frame_num].append(data)
            print(f"Page {page_num} loaded into Frame {frame_num}")

    else:
        print(f"Page number {page_num} out of bounds!")
        return

    updateTLB(page_num, frame_num, trans_lb)
    updatePageTable(page_num, frame_num, page_dir)

def updateTLB(page_num, frame_num, trans_lb):
    if len(trans_lb) < 16:
        trans_lb.append([page_num, frame_num])
    else:
        trans_lb.pop(0)
        trans_lb.append([page_num, frame_num])
    print(f"TLB updated: Page {page_num}, Frame {frame_num}")

def updatePageTable(page_num, frame_num, page_dir):
    if len(page_dir) < 256:
        page_dir.append([page_num, frame_num])
    else:
        page_dir.pop(0)
        page_dir.append([page_num, frame_num])
    print(f"Page Table updated: Page {page_num}, Frame {frame_num}")

def refreshTLB(latest_index, trans_lb):
    trans_lb.append(trans_lb.pop(latest_index))
    print("TLB refreshed with LRU")

def refreshPageTable(latest_index, page_dir):
    page_dir.append(page_dir.pop(latest_index))
    print("Page Table refreshed with LRU")

def accessPhysicalMem(frame_num, offset, phys_mem):
    if frame_num < 256 and offset < 256:
        byte_data = phys_mem[frame_num][offset]
        print(f"Read from Physical Memory: Frame {frame_num}, Offset {offset}, Data {byte_data}")
        return byte_data
    else:
        print("Frame number or offset out of bounds")
