Virtual Memory Manager

Project Overview

This project involves the creation of a Virtual Memory Manager responsible for translating logical addresses into physical addresses. It utilizes a Translation Lookaside Buffer (TLB) and a page table for efficient address translation. The program reads logical addresses from an input file, performs the translation, and retrieves the byte value stored at the corresponding physical address.

Understanding the Problem

In this Virtual Memory Manager:
Logical Address: Comprises a page number and an offset.
Physical Address: Consists of a frame number and an offset.
Key Steps
Extract the page number from the logical address.
Determine the corresponding frame number using the page number.
Check the TLB for a hit. If a TLB hit occurs, retrieve the frame number from the TLB.
If there's a TLB miss, consult the page table. If the page table has a hit, obtain the frame number.
In case of a page fault, handle it by reading data from a hard drive representation (BACKING_STORE.bin) with the corresponding page number. Allocate the data in physical memory in an available frame. Update the TLB and page table with the frame number and page number.
Concatenate the frame number and offset to obtain the physical address.
Using the frame number and offset, extract the data from physical memory.
System Configuration
Page table with 256 entries.
Page size set at 256 bytes.
TLB with 16 entries.
Frame size of 256 bytes.
256 frames available.
Physical memory size of 65,536 bytes (256 frames * 256-byte frame size).
Implementation in Python 3.6.
Data represented as integers.
TLB (Translation Lookaside Buffer) and Page Table implemented as lists.
Physical Memory organized using a dictionary.
Hard drive representation with a Binary File (BACKING_STORE.bin).
Input/Output managed through Text Files (address.txt for input; output.txt for output).
TLB and Page Table are updated using the LRU (Least Recently Used) algorithm.

Results and Analysis

The program generates and records the following values in output.txt:
Logical address under translation.
Corresponding physical address.
The byte value is stored at the physical address.
Page-fault rate: The percentage of address references resulting in page faults.
TLB hit rate: The percentage of address references resolved through the TLB.
This Virtual Memory Manager efficiently handles logical-to-physical address translation and page faults, optimizing memory management using a TLB, page table, and a hard drive representation.