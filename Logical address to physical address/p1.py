import p2

def tlbLookup(page_number, phys_mem, offset, log_addr, trans_lb, read_count, out_file):
    for index in range(len(trans_lb)):
        if page_number == trans_lb[index][0]:
            print(f"TLB hit for Page Number: {page_number}")
            frame_num = trans_lb[index][1]
            byte_data = p2.accessPhysicalMem(frame_num, offset, phys_mem)
            phys_addr = int(f'{frame_num:08b}{offset:08b}', 2)
            output_str = f"{read_count} Logical: {log_addr} Physical: {phys_addr} Value: {byte_data}\n"
            print(output_str)
            out_file.write(output_str)
            p2.refreshTLB(index, trans_lb)
            return 1
    return 0

def pageTableLookup(page_num, log_addr, offset, read_count, page_dir, phys_mem, out_file):
    for entry in range(len(page_dir)):
        if page_num == page_dir[entry][0]:
            print(f"Page Table hit for Page Number: {page_num}")
            frame_num = page_dir[entry][1]
            byte_data = p2.accessPhysicalMem(frame_num, offset, phys_mem)
            phys_addr = int(f'{frame_num:08b}{offset:08b}', 2)
            output_str = f"{read_count} Logical: {log_addr} Physical: {phys_addr} Value: {byte_data}\n"
            print(output_str)
            out_file.write(output_str)
            p2.refreshPageTable(entry, page_dir)
            return 1
    return 0
