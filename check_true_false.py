import time
from copy import deepcopy
from LogicalExpression_given import *

def main(argv):

    #unique_symbols = set()
    model_map = dict()
    if len(argv) != 4:
        print('Usage: %s [wumpus-rules-file] [additional-knowledge-file] [input_file]' % argv[0])
        sys.exit(0)

    # Read wumpus rules file
    try:
        input_file = open(argv[1], 'rb')
    except:
        print('failed to open file %s' % argv[1])
        sys.exit(0)

    # Create the knowledge base with wumpus rules
    print '\nLoading wumpus rules...'
    knowledge_base = LogicalExpression()
    knowledge_base.connective = ['and']
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # A mutable counter so recursive calls don't just make a copy
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Read additional knowledge base information file
    try:
        input_file = open(argv[2], 'rb')
    except:
        print('failed to open file %s' % argv[2])
        sys.exit(0)

    # Add expressions to knowledge base
    print 'Loading additional knowledge...'
    for line in input_file:
        # Skip comments and blank lines. Consider all line ending types.
        if line[0] == '#' or line == '\r\n' or line == '\n' or line == '\r':
            continue
        counter = [0]  # a mutable counter
        subexpression = read_expression(line.rstrip('\r\n'), counter)
        knowledge_base.subexpressions.append(subexpression)
    input_file.close()

    # Verify it is a valid logical expression
    if not valid_expression(knowledge_base):
        sys.exit('invalid knowledge base')

    # I had left this line out of the original code. If things break, comment out.
    #print_expression(knowledge_base, '\n')



    # Read statement whose entailment we want to determine
    try:
        input_file = open(argv[3], 'rb')
    except:
        print('failed to open file %s' % argv[3])
        sys.exit(0)
    print 'Loading statement...'
    input_statement = input_file.readline().rstrip('\r\n')
    input_file.close()

    # Convert statement into a logical expression and verify it is valid
    counter = [0]
    statement = read_expression(input_statement, counter)
    if not valid_expression(statement):
        sys.exit('invalid statement')

    negate_input = '(not %s)' %(input_statement)
    counter = [0]
    negate_statement = read_expression(negate_input, counter)
    if not valid_expression(negate_statement):
        sys.exit('Negate statement invalid')

    #start = time.time()
    unique_symbols = create_unique_symbol_list(knowledge_base,statement)
    #########################
    unique_symbols, model_map = update_model(knowledge_base,unique_symbols,model_map)
    #########################
    #end = time.time()
    #print 'rohan:', (end-start)
    print '\nChecking statement: ',
    print_expression(statement, '')
    print

    start2 = time.time()
    definitely_true  = tt_check_all(knowledge_base,statement,list(unique_symbols),model_map)
    definitely_false = tt_check_all(knowledge_base,negate_statement,list(unique_symbols),model_map)
    print 'definitely true:', definitely_true
    print 'definitely false:', definitely_false
    end2 = time.time()
    print 'time to check entail:', (end2-start2)

    fp = open('result.txt','w')
    if definitely_true:
        fp.write('definitely true')
    if definitely_false:
       fp.write('definitely false')
    if (not definitely_true) and (not definitely_false):
        fp.write('possibly true, possibly false')
    if definitely_true and definitely_false:
        fp.write('both true and false')
    fp.close()
    # Show us what the statement is


    # Run the statement through the inference engine
    #check_true_false(knowledge_base, statement)

    sys.exit(1)

def create_unique_symbol_list(knowledge_base, alpha):
    #temp = []

    temp = get_symbols(knowledge_base)
    temp = temp + get_symbols(alpha)
    return set(temp)

def get_symbols(statement):
    list_temp = []

    if statement.symbol[0]:
        list_temp.append(statement.symbol[0])
    else:
        for subex in statement.subexpressions:
            list_temp = list_temp + get_symbols(subex)
    return list_temp

#map key - symbol value - boolean
def pl_true(statement, model_map):
    result_bool = None
    if statement.connective[0] == '' and statement.symbol[0] != '':
        try:
            result_bool = model_map[statement.symbol[0]]
        except:
            print 'error'

    elif statement.connective[0] == 'and':
        result_bool = True
        list_temp = []
        for child in statement.subexpressions:
            list_temp.append(pl_true(child,model_map))
        for r in list_temp:
            result_bool = result_bool and r

    elif statement.connective[0] == 'or':
        result_bool = False
        list_temp = []
        for child in statement.subexpressions:
            list_temp.append(pl_true(child,model_map))
        for r in list_temp:
            result_bool = result_bool or r

    elif statement.connective[0] == 'xor':
        result_bool = False
        list_temp = []
        for child in statement.subexpressions:
            list_temp.append(pl_true(child,model_map))
        for r in list_temp:
            result_bool = result_bool != r

    elif statement.connective[0] == 'not':
        result_bool = not (pl_true(statement.subexpressions[0], model_map))

    elif statement.connective[0] == 'if':
        result_bool = (not pl_true(statement.subexpressions[0],model_map)) or pl_true(statement.subexpressions[1],model_map)

    elif statement.connective[0] == 'iff':
        result_bool = pl_true(statement.subexpressions[0],model_map) == pl_true(statement.subexpressions[1],model_map)

    return result_bool

def tt_check_all(knowledge_b, alpha, symbols, model):
    if len(symbols) == 0:
        if pl_true(knowledge_b, model):
            return pl_true(alpha, model)
        else:
            return True
    else:
        first = symbols.pop()
        temp = tt_check_all(knowledge_b, alpha, deepcopy(symbols), extend(first,True, deepcopy(model))) and \
               tt_check_all(knowledge_b, alpha, deepcopy(symbols), extend(first,False, deepcopy(model)))
        return temp

def extend(symbol, value, model):
    model[symbol] = value
    return model

def update_model(kb, unique_symbols, model_map):
    for subexpression in kb.subexpressions:
        if subexpression.connective[0] == 'not':
            sym = subexpression.subexpressions[0].symbol
            model_map[sym[0]] = False
            unique_symbols.discard(sym[0])
        elif subexpression.connective[0] == '':
            sym = subexpression.symbol
            model_map[sym[0]] = True
            unique_symbols.discard(sym[0])
    return unique_symbols, model_map

if __name__ == '__main__':
    main(sys.argv)