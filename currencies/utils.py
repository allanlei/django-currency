from decimal import Decimal


def format(value, symbol='$', positive_format=u'{symbol}{value}', negative_format=u'({symbol}{value})', decimal_symbol='.', digit_group_symbol=',', rounding=2, thousands=3, group_digits=True, **kwargs):

    value = Decimal(value)
    if rounding is not None and rounding > 0:
        value = value.quantize(Decimal(10) ** -rounding)

    negative, digits, exp = value.as_tuple()
    numbers, decimals = ''.join(map(str, digits[:exp])),''.join(map(str, digits[exp:]))
    
    if group_digits and digit_group_symbol is not None:
        s = numbers[::-1]
        groups = []
        i = 0
        while i < len(s):
            h = i
            i += thousands
            groups.append(s[h:i])
            
        numbers = digit_group_symbol.join(groups)[::-1]
    return (negative and negative_format or positive_format).format(symbol=symbol, value=decimal_symbol.join([numbers, decimals]))
