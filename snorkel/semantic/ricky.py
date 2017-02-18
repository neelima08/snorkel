from __future__ import print_function

from pdb import set_trace as t
from grammar import Rule

# Helpers ======================================================================
def sems0(sems):
    return sems[0]

def sems1(sems):
    return sems[1]

def sems_in_order(sems):
    return tuple(sems)

def sems_reversed(sems):
    return tuple(reversed(sems))

# Rules ======================================================================
lexical_rules = [
    # arg
    Rule('$Arg', 'arg', '.arg'),
    Rule('$Arg', 'argument', '.arg'),
    # logic
    Rule('$And', 'and', '.and'),
    Rule('$All', 'all', '.all'),
    Rule('$IntToBool', 'a', ('.atleast', ('.int', 1))),
    Rule('$Int', 'a', ('.int', 1)),
    Rule('$Int', 'no', ('.int', 0)),
    # direction
    Rule('$Sentence', '?in ?the sentence', '.sentence_tokens'),
    # other
    Rule('$In', 'in', '.in'),
    Rule('$Label', 'label ?it', '.label'),
]

lexical_rules.extend(
    [Rule('$True', w, ('.bool', True)) for w in ['true', 'correct']] +
    [Rule('$False', w, ('.bool', False)) for w in ['false', 'incorrect', 'wrong']] +
    [Rule('$Or', w, '.or') for w in ['or', 'nor']] +
    [Rule('$Any', w, '.any') for w in ['any', 'a']] +
    [Rule('$Not', w, '.not') for w in ['not', "n't"]] +
    [Rule('$None', w, '.none') for w in ['none', 'not any', 'neither', 'no']] +
    [Rule('$Is', w) for w in ['is', 'are', 'be']] +
    [Rule('$Because', w) for w in ['because', 'since', 'if']] +
    [Rule('$Upper', w, '.upper') for w in ['upper', 'uppercase', 'upper case', 'all caps', 'all capitalized']] +
    [Rule('$Lower', w, '.lower') for w in ['lower', 'lowercase', 'lower case']] +
    [Rule('$Capital', w, '.capital') for w in ['capital', 'capitals', 'capitalized']] +
    [Rule('$Equals', w, '.equals') for w in ['equal', 'equals', '=', '==', 'same ?as', 'identical']] + 
    [Rule('$LessThan', w, '.less') for w in ['less than', 'smaller than', '<']] +
    [Rule('$AtMost', w, '.atmost') for w in ['at most', 'no larger than', 'less than or equal', 'within', 'no more than', '<=']] +
    [Rule('$MoreThan', w, '.more') for w in ['more than', 'greater than', 'larger than', '>']] + 
    [Rule('$AtLeast', w, '.atleast') for w in ['at least', 'no less than', 'no smaller than', 'greater than or equal', '>=']] +
    [Rule('$Exists', w) for w in ['exist', 'exists']] +
    [Rule('$Contains', w, '.contains') for w in ['contains', 'contain']] +
    [Rule('$StartsWith', w, '.startswith') for w in ['starts with', 'start with']] +
    [Rule('$EndsWith', w, '.endswith') for w in ['ends with', 'end with']] +
    [Rule('$Left', w, '.left_tokens') for w in ['left', 'before', 'precedes', 'preceding']] +
    [Rule('$Right', w, '.right_tokens') for w in ['right', 'after', 'follows', 'following']] +
    [Rule('$Between', w, '.between_tokens') for w in ['between', 'inbetween']] +
    [Rule('$Separator', w) for w in [',', ';', '/']] +
    [Rule('$Count', w, '.count') for w in ['number', 'length', 'count']] +
    [Rule('$Word', w) for w in ['word', 'words', 'term']] + 
    [Rule('$NounPOS', w, ('.string', 'NN')) for w in ['noun', 'nouns']] +
    [Rule('$DateNER', w, ('.string', 'DATE')) for w in ['date', 'dates']] +
    [Rule('$NumberPOS', w, ('.string', 'CD')) for w in ['number', 'numbers']] +
    [Rule('$PersonNER', w, ('.string', 'PERSON')) for w in ['person', 'people']] +
    [Rule('$LocationNER', w, ('.string', 'LOCATION')) for w in ['location', 'locations', 'place', 'places']] +
    [Rule('$OrganizationNER', w, ('.string', 'ORGANIZATION')) for w in ['organization', 'organizations']] +
    [Rule('$Punctuation', w) for w in ['.', ',', ';', '!', '?']]
    )

unary_rules = [
    Rule('$Bool', '$BoolLit', sems0),
    Rule('$BoolLit', '$True', sems0),
    Rule('$BoolLit', '$False', sems0),
    Rule('$Conj', '$And', sems0),
    Rule('$Conj', '$Or', sems0),
    Rule('$Exists', '$Is'),
    Rule('$Equals', '$Is', '.equals'),
    Rule('$Inequals', '$LessThan', sems0),
    Rule('$Inequals', '$AtMost', sems0),
    Rule('$Inequals', '$MoreThan', sems0),
    Rule('$Inequals', '$AtLeast', sems0),
    Rule('$Compare', '$Inequals', sems0),
    Rule('$Compare', '$Equals', sems0),
    Rule('$Direction', '$Left', sems0),
    Rule('$Direction', '$Right', sems0),
    Rule('$POS', '$NounPOS', sems0),
    Rule('$POS', '$NumberPOS', sems0),
    Rule('$NER', '$DateNER', sems0),
    Rule('$NER', '$PersonNER', sems0),
    Rule('$NER', '$LocationNER', sems0),
    Rule('$NER', '$OrganizationNER', sems0),
    Rule('$StringList', '$UserList', sems0),
    Rule('$UnaryStringToBool', '$Lower', sems0),
    Rule('$UnaryStringToBool', '$Upper', sems0),
    Rule('$UnaryStringToBool', '$Capital', sems0),
    Rule('$BinaryStringToBool', '$StartsWith', sems0),
    Rule('$BinaryStringToBool', '$EndsWith', sems0),
    Rule('$BinaryStringToBool', '$In', sems0),
    Rule('$BinaryStringToBool', '$Contains', sems0),
    Rule('$BinaryStringToBool', '$Equals', sems0),
    # ArgX may be treated as an object or a string (referring to its textual contents)
    Rule('$String', '$ArgX', lambda sems: ('.arg_to_string', sems[0])),
    Rule('$StringList', 'StringListOr', sems0),
    Rule('$StringList', 'StringListAnd', sems0),
    Rule('$List', '$BoolList', sems0),
    Rule('$List', '$StringList', sems0),
    Rule('$List', '$IntList', sems0),
    Rule('$List', '$TokenList', sems0),
    # Rule('$List', '$POSList', sems0),
    # Rule('$List', '$NERList', sems0),
    # Rule('$List', '$CIDList', sems0),
    Rule('$ROOT', '$LF', lambda sems: ('.root', sems[0])),
]

compositional_rules = [
    Rule('$LF', '$Label $Bool $Because $Bool', lambda sems: (sems[0], sems[1], sems[3])),
    
    # Logicals
    Rule('$Bool', '$Bool $Conj $Bool', lambda sems: (sems[1], sems[0], sems[2])),
    Rule('$Bool', '$Not $Bool', sems_in_order),
    Rule('$Bool', '$All $BoolList', sems_in_order),
    Rule('$Bool', '$Any $BoolList', sems_in_order),
    Rule('$Bool', '$None $BoolList', sems_in_order),

    # Strings
        # building strings
    Rule('$StringStub', '$Quote $QueryToken', lambda sems: [sems[1]]),
    Rule('$StringStub', '$StringStub $QueryToken', lambda sems: sems[0] + [sems[1]]),
    Rule('$String', '$StringStub $Quote', lambda sems: ('.string', ' '.join(sems[0]))),

        # building string lists (TODO: remove some redundancies here?)
    Rule('$StringList', '$String ?$Separator $String', lambda sems: ('.list', sems[0], sems[2])),
    Rule('$StringList', '$StringList ?$Separator $String', lambda sems: tuple((list(sems[0]) + [sems[2]]))),
    
    Rule('$StringListOr', '$String ?$Separator $Or $String', lambda sems: ('.list', sems[0], sems[3])),
    Rule('$StringListOr', '$StringList ?$Separator $Or $String', lambda sems: tuple(list(sems[0]) + [sems[3]])),

    Rule('$StringListOr', '$String ?$Separator $And  $String', lambda sems: ('.list', sems[0], sems[3])),
    Rule('$StringListAnd', '$StringList ?$Separator $And $String', lambda sems: tuple(list(sems[0]) + [sems[3]])),

        # applying $StringToBool functions
    Rule('$Bool', '$String $StringToBool', lambda sems: ('.call', sems[1], sems[0])),
    Rule('$Bool', '$StringListOr $StringToBool', lambda sems: ('.or', ('.map', sems[1], sems[0]))),
    Rule('$Bool', '$StringListAnd $StringToBool', lambda sems: ('.and', ('.map', sems[1], sems[0]))),
    Rule('$BoolList', '$StringList $StringToBool', lambda sems: ('.map', sems[1], sems[0])),

        # defining $StringToBool functions
    Rule('$StringToBool', '$UnaryStringToBool', lambda sems: (sems[0],)),
    Rule('$StringToBool', '$BinaryStringToBool $String', lambda sems: (sems[0], sems[1])),
    Rule('$StringToBool', '$BinaryStringToBool $StringListAnd', lambda sems: ('.composite_and', (sems[0],), sems[1])),
    Rule('$StringToBool', '$BinaryStringToBool $StringListOr', lambda sems:  ('.composite_or',  (sems[0],), sems[1])),
    Rule('$StringToBool', '$In $StringList', sems_in_order),
    
    # Integers
        # applying $IntoToBool functions
    Rule('$Bool', '$Int $IntToBool', lambda sems: ('.call', sems[1], sems[0])),
    Rule('$BoolList', '$IntList $IntToBool', lambda sems: ('.map', sems[1], sems[0])),
    
    # e.g., more than five of X words are upper
    Rule('$Bool', '$Compare $Int $BoolList', lambda sems: ('.call', (sems[0], sems[1]), ('.sum', sems[2]))),

    Rule('$IntToBool', '$In $IntList', sems_in_order),
    Rule('$IntToBool', '$Contains $Int', sems_in_order),
    Rule('$IntToBool', '$Compare $Int', sems_in_order),

        # count
    Rule('$Int', '$Count $List', sems_in_order),
    Rule('$Bool', '$IntToBool $List', lambda sems: ('.call', sems[0], ('.count', sems[1]))), # There are at least two nouns to the left...
    # Rule('$Bool', '$Exists $Int $List', lambda sems: ('.call', ('.equals', sems[1]), ('.count', sems[2]))), # There are three nouns to the left...
    Rule('$Bool', '$IntToBool $POS $Exists $TokenList', lambda sems: 
        ('.call', sems[0], ('.count', ('.filter_attr', sems[3], ('.string', 'pos_tags'), sems[1])))), # At least one noun is to the left...
    Rule('$Bool', '$IntToBool $NER $Exists $TokenList', lambda sems: 
        ('.call', sems[0], ('.count', ('.filter_attr', sems[3], ('.string', 'ner_tags'), sems[1])))), # At least one noun is to the left...
    # Rule('$Bool', '$Exists $List', lambda sems: ('.call', ('.atleast', ('.int', 1)), ('.count', sems[1]))),
    
    # Context
    Rule('$ArgX', '$Arg $Int', sems_in_order),

    Rule('$TokenList', '$Direction $ArgX', sems_in_order),
    Rule('$TokenList', '$Between $ArgX $And $ArgX', lambda sems: (sems[0], sems[1], sems[3])),
    Rule('$TokenList', '$Sentence', lambda sems: (sems[0],)),
    
    Rule('$StringList', '$TokenList', lambda sems: ('.field', sems[0], ('.string', 'words'))),
    Rule('$TokenList', '$Word $TokenList', lambda sems: ('.filter_words', sems[1], ('.string', 'words'))),
    Rule('$TokenList', '$POS $TokenList', lambda sems: ('.filter_attr', sems[1], ('.string', 'pos_tags'), sems[0])),
    Rule('$TokenList', '$POS $TokenList', lambda sems: ('.filter_attr', sems[1], ('.string', 'ner_tags'), sems[0])),
    # Rule('$NERList', '$NER $TokenList', lambda sems: ('.field', sems[1], '')),

    # Slices
    # TODO: Test these more thoroughly
    # Rule('$String', '$Int $StringList', lambda sems: ('.index', sems[1], sems[0])),
    # Rule('$StringList', '$LessThan $Int $StringList', lambda sems: ('.slice', sems[2], ('.int', 0), sems[1])),
    # Rule('$StringList', '$AtMost $Int $StringList', lambda sems: ('.slice', sems[2], ('.int', 0), ('.int', sems[1][1] + 1))),
    # Rule('$StringList', '$AtLeast $Int $StringList', lambda sems: ('.slice', sems[2], sems[1], 100)),
    # Rule('$StringList', '$MoreThan $Int $StringList', lambda sems: ('.slice', sems[2], ('.int', sems[1][1] + 1), 100)),
    # Rule('$Int', '$Int $IntList', lambda sems: ('.index', sems[1], sems[0])),

    # Context
    # Note: Normal 'X in Y' does not work because we need to know what they are looking for (e.g., words, pos, ner)
    # Rule('$StringList', '$Word $Direction $ArgX', lambda sems: (sems[1], sems[2], sems[0])),
    # Rule('$StringList', '$Direction $ArgX $Or $ArgX', lambda sems: ('.merge', (sems[0], sems[1], ('.string', 'words')), (sems[0], sems[3], ('.string', 'words')))),
    # Rule('$StringToBool', '$Direction $ArgX', lambda sems: ('.in', (sems[0], sems[1], ('.string', 'words')))),
    
    # Rule('$Bool', '$POS ?$In $Direction $ArgX', lambda sems: ('.in', (sems[2], sems[3], ('.string', 'pos_tags')), sems[0])),
    # Rule('$Bool', '$NER ?$In $Direction $ArgX', lambda sems: ('.in', (sems[2], sems[3], ('.string', 'ner_tags')), sems[0])),
    
    # Rule('$StringList', '$Between $ArgX $And $ArgX', lambda sems: (sems[0], sems[1], sems[3], ('.string', 'words'))),
    # Rule('$StringToBool', '$Between $ArgX $And $ArgX', lambda sems: ('.in', (sems[0], sems[1], sems[3], ('.string', 'words')))),
    
    # Rule('$Bool', '$POS ?$In $Between $ArgX $And $ArgX', lambda sems: ('.in', (sems[2], sems[3], sems[5], ('.string', 'pos_tags')), sems[0])),
    # Rule('$Bool', '$NER ?$In $Between $ArgX $And $ArgX', lambda sems: ('.in', (sems[2], sems[3], sems[5], ('.string', 'ner_tags')), sems[0])),
    
    # Rule('$StringList', '$Sentence ?$ArgX ?$And ?$ArgX', lambda sems: (sems[0], ('.string', 'words'))),
    
    # Rule('$Bool', '$POS ?$In $Sentence ?$ArgX ?$And ?$ArgX', lambda sems: ('.in', (sems[2], ('.string', 'pos_tags')), sems[0])),
    # Rule('$Bool', '$NER ?$In $Sentence ?$ArgX ?$And ?$ArgX', lambda sems: ('.in', (sems[2], ('.string', 'ner_tags')), sems[0])),
]

snorkel_rules = lexical_rules + unary_rules + compositional_rules

snorkel_ops = {
    # root
    '.root': lambda x: lambda c: x(c),
    '.label': lambda x, y: lambda c: (1 if x(c)==True else -1) if y(c)==True else 0,
    # primitives
    '.bool': lambda x: lambda c: x,
    '.string': lambda x: lambda c: x,
    '.int': lambda x: lambda c: x,
    # lists
    '.list': lambda *x: lambda c: [z(c) for z in x],
    '.user_list': lambda x: lambda c: c['user_lists'][x(c)],
        # apply a function x to elements in list y
    '.map': lambda x, y: lambda cxy: [x(cxy)(lambda c: yi)(cxy) for yi in y(cxy)],
    '.call': lambda *x: lambda c: x[0](c)(x[1])(c), #TODO: extend to more than one argument?
        # apply an element to a list of functions (then call 'any' or 'all' to convert to boolean)
    '.composite_and': lambda x, y: lambda cxy: lambda z: lambda cz: all([x(lambda c: yi)(cxy)(z(cz)) for yi in y(cxy)]), # apply
    '.composite_or':  lambda x, y: lambda cxy: lambda z: lambda cz: any([x(lambda c: yi)(cxy)(z(cz)) for yi in y(cxy)]), # apply
    # logic
    '.and': lambda *x: lambda c: all(xi(c)==True for xi in x),
    '.or': lambda *x: lambda c: any(xi(c)==True for xi in x),
    '.not': lambda x: lambda c: not x(c),
    '.all': lambda x: lambda c: all(xi==True for xi in x(c)),
    '.any': lambda x: lambda c: any(xi==True for xi in x(c)),
    '.none': lambda x: lambda c: not any(xi==True for xi in x(c)),
    # comparisons
    '.equals': lambda x: lambda cx: lambda y: lambda cy: y(cy) == x(cx),
    '.less': lambda x: lambda cx: lambda y: lambda cy: y(cy) < x(cx),
    '.atmost': lambda x: lambda cx: lambda y: lambda cy: y(cy) <= x(cx),
    '.more': lambda x: lambda cx: lambda y: lambda cy: y(cy) > x(cx),
    '.atleast': lambda x: lambda cx: lambda y: lambda cy: y(cy) >= x(cx),
    # string functions
    '.upper': lambda c: lambda x: lambda cx: x(cx).isupper(),
    '.lower': lambda c: lambda x: lambda cx: x(cx).islower(),
    '.capital': lambda c: lambda x: lambda cx: x(cx)[0].isupper(),
    '.startswith': lambda x: lambda cx: lambda y: lambda cy: y(cy).startswith(x(cx)),
    '.endswith': lambda x: lambda cx: lambda y: lambda cy: y(cy).endswith(x(cx)),
    # lists
    '.in': lambda x: lambda cx: lambda y: lambda cy: y(cy) in x(cx),
    '.contains': lambda x: lambda cx: lambda y: lambda cy: x(cx) in y(cy),
    '.count': lambda x: lambda c: len(x(c)),
    '.sum': lambda x: lambda c: sum(x(c)),
        # '.index': lambda x, y: lambda c: x(c)[max(0, y(c) - 1)], # account for 0-indexing 
        # '.slice': lambda x, y, z: lambda c: x(c)[y(c):z(c)], 
        # '.merge': lambda x, y: lambda c: x(c) + y(c),
    # context
    '.arg': lambda x: lambda c: c['candidate'][x(c) - 1],
        # For ease of testing, temporarily allow tuples of strings in place of legitimate candidates
    '.arg_to_string': lambda x: lambda c: x(c) if isinstance(x(c), basestring) else x(c).get_span(),
    '.left_tokens': lambda x: lambda c: c['lf_helpers']['get_left_tokens'](x(c)),
    '.right_tokens': lambda x: lambda c: c['lf_helpers']['get_right_tokens'](x(c)),
    '.between_tokens': lambda x, y: lambda c: c['lf_helpers']['get_between_tokens'](x(c), y(c)),
    '.sentence_tokens': lambda c: c['lf_helpers']['get_sentence_tokens'](c['candidate'][0]),
    '.field': lambda toklist, attr: lambda c: [getattr(t, attr(c)) for t in toklist(c)],
    '.filter_attr': lambda toklist, attr, val: lambda c: [t for t in toklist(c) if getattr(t, attr(c)) == val(c)],
    '.filter_words': lambda toklist, attr: lambda c: [t for t in toklist(c) if any(letter.isalnum() for letter in getattr(t, attr(c)))],
    }