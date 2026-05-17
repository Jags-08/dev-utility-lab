
#include <iostream>
#include <string>

extern "C" {
    bool check_memory_integrity(long allocations, long frees) {
        if (allocations != frees) {
            std::cerr << "Memory drift detected: " << (allocations - frees) << std::endl;
            return false;
        }
        return true;
    }
}
