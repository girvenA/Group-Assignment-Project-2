from phplex import analyze_code
from phpparser import parse

# Function to analyze and interpret input code
def interpret_code(code):
    tokens = analyze_code(code)
    result = parse(code)
    return result

# Main function to run the lexer and parser
if __name__ == '__main__':
    code = '''
    <?php
    PRINT "List of Odd Number 1-100:\n";
    $num=1;
    WHILE ($num<=100) {
        IF (($num % 2)!=0) {
            PRINT "".$num." ";
        }
        $num=$num+1;
    }
    ?>
    '''
    interpret_code(code)