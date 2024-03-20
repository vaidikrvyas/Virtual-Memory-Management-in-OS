This Python program simulates three popular page replacement algorithms commonly used in operating systems to manage physical memory. It takes as input the number of frames or total frame count and a page reference string, then proceeds to simulate the respective page replacement algorithms, which include First-In-First-Out (FIFO), Least Recently Used (LRU), and Optimal. The program calculates and provides page fault statistics, offering users insights into how these algorithms handle memory management and their respective page fault rates.


FIFO Page Replacement Algorithm

Introduction
The FIFO page replacement algorithm manages physical memory by replacing the oldest page in memory when a page fault occurs. This program helps you understand how FIFO works and calculates the page fault rate for a given page reference string.

LRU Page Replacement Algorithm Simulator

Introduction
The LRU page replacement algorithm manages physical memory by replacing the least recently used page in memory when a page fault occurs. This program helps you understand how LRU works and calculates the page fault rate for a given page reference string.

Optimal Page Replacement Algorithm Simulator

Introduction
The Optimal page replacement algorithm manages physical memory by replacing the page that will not be used for the longest time in the future when a page fault occurs. This program helps you understand how Optimal works and calculates the page fault rate for a given page reference string.

Usage

Input Number of Frames: Start the program and input the number of frames available in physical memory. Provide an integer value and press Enter.
Input Page Reference String: The program will prompt you to enter the page reference string, where pages are separated by spaces. This input represents the sequence of pages the program will access.
Output and Analysis: After processing the page reference string, the program will generate a table displaying the page reference string, the frames currently in memory, and whether a page fault occurred for each page reference. Additionally, the program will provide statistical information, including the total number of page requests, the total page faults incurred, and the resulting page fault rate.
This unified usage guide outlines the common steps and functionality for all three page replacement algorithms (FIFO, LRU, and Optimal) within your Virtual Memory Management program.








