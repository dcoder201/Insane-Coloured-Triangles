def triangle(row):
    colors = [0 if c == 'R' else 1 if c == 'G' else 2 for c in row]
    
    # Loop through the rows, generating each new row based on the previous one
    while len(colors) > 1:
        new_colors = []
        for i in range(len(colors) - 1):
            if colors[i] == colors[i+1]:
                new_colors.append(colors[i])
            else:
                new_colors.append(3 - colors[i] - colors[i+1])
        colors = new_colors
    
    # Convert the last remaining color back to its corresponding character and return it as a string
    return 'R' if colors[0] == 0 else 'G' if colors[0] == 1 else 'B'
  
  
 def _test(cases):
    for _in, _out in cases:
        test.assert_equals(triangle(_in), _out)

test.describe('Insane Coloured Triangles')
basic_cases = [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G']
]
test.it('Basic Tests')
_test(basic_cases)
