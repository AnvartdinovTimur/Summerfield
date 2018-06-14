import sys


Zero = ['  ***  ', ' *   * ', '*     *', '*     *', '*     *', ' *   * ', '  ***  ']
One = [' * ', '** ', ' * ', ' * ', ' * ', ' * ', '***']
Two = [' *** ', '*   *', '*  * ', '  *  ', ' *   ', '*    ', '*****']
Three = [' *** ', '*   *', '    *', '  ** ', '    *', '*   *', ' *** ']
Four = ['   *  ', '  **  ', ' * *  ', '*  *  ', '******', '   *  ', '   *  ']
Five = ['*****', '*    ', '*    ', ' *** ', '    *', '*   *', ' *** ']
Six = [' *** ', '*    ', '*    ', '**** ', '*   *', '*   *', ' *** ']
Seven = ['*****', '    *', '   * ', '  *  ', ' *   ', '*    ', '*    ']
Eight = [' *** ', '*   *', '*   *', ' *** ', '*   *', '*   *', ' *** ']
Nine = [' ****', '*   *', '*   *', ' ****', '    *', '    *', '    *']

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ''
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            i = 0
            line_num = digit[row]
            line_num_fin = ''
            while i < len(line_num):
                if line_num[i] == '*':
                    line_num_fin += str(number)
                else:
                    line_num_fin += ' '
                i += 1
            line += line_num_fin + '  '
            column += 1
        print(line)
        row += 1
except IndexError:
    print('Вводите bidigits.py <number>')
except ValueError as err:
    print(err, 'in', digits)
