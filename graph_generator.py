# File: graph_generator.py
import matplotlib.pyplot as plt
from performance_tests import measure_insert_time, measure_scan_time, measure_bst_range

sizes = [100, 1000, 10000, 100000]

def collect_data():
    inserts = []
    scans = []
    bst = []
    for n in sizes:
        inserts.append(measure_insert_time(n) * 1000)
        scans.append(measure_scan_time(n) * 1000)
        bst.append(measure_bst_range(n) * 1000)
    return inserts, scans, bst

def generate_graphs():
    inserts, scans, bst = collect_data()

    # 1. O(N) vs O(logN)
    plt.figure()
    plt.plot(sizes, scans, label="Hash Table Scan O(N)")
    plt.plot(sizes, bst, label="BST Range Query O(logN)")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("N")
    plt.ylabel("Time (ms)")
    plt.title("O(N) vs O(logN) Performance")
    plt.legend()
    plt.savefig("comparison_on_vs_log.png")

    # 2. Insert Performance
    plt.figure()
    plt.plot(sizes, inserts)
    plt.xscale("log")
    plt.xlabel("N")
    plt.ylabel("Avg Insert Time (ms)")
    plt.title("Insert Performance (Hash+BST)")
    plt.savefig("insert_performance.png")

    print("Graphs saved: comparison_on_vs_log.png and insert_performance.png")

if __name__ == "__main__":
    generate_graphs()
