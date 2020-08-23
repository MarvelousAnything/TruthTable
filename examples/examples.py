from bin import truth_table, print_truth_table
import bin

print_truth_table(*truth_table(bin.xor))
print_truth_table(*truth_table(bin.half_adder))
print_truth_table(*truth_table(bin.full_adder))
