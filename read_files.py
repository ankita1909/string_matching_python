ref_filename = 'ref.txt'
output_filename = 'output.txt'
list_of_instruction = []
with open(ref_filename, 'r') as f:
    refs = f.readlines()

with open(output_filename, 'r') as f:
    output = f.readlines()
    
    for ref in refs:
        for line in output:
            if ref in line:
                list_of_instruction.append(ref)
                break
for i in list_of_instruction:
    print(i)