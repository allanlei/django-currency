# -*- coding: utf-8 -*-

SYMBOL = 'symbol'
POSITIVE_FORMAT = 'positive_format'
NEGATIVE_FORMAT = 'negative_format'
DECIMAL_SYMBOL = 'decimal_symbol'
DIGIT_GROUP_SYMBOL = 'digit_group_symbol'
GROUP_DIGITS = 'group_digits'
	
	
CURRENCIES = {
    'AED': {
		SYMBOL: u'د.إ.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'United Arab Emirates dirham',
        'countries': ['United Arab Emirates', 'AE'],
    },
    'AFN': {
		SYMBOL: u'؋',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Afghan afghani',
		'countries': ['AF']
    },
    'ALL': {
		SYMBOL: u'Lek',
		POSITIVE_FORMAT: u'{value}{symbol}',
		NEGATIVE_FORMAT: u'-{value}{symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Albanian lek',
		'countries': ['AL']
    },
    'AMD': {
		SYMBOL: u'դր.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Armenian dram',
		'countries': ['AM']
    },
    'ANG': {
        'name': 'Netherlands Antillean guilder',
        SYMBOL: u'ƒ',
        POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'countries': ['Curaçao, Sint Maarten']
    },
    'AOA': {
        'name': 'Angolan kwanza',
        SYMBOL: u'Kz',
        POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'countries': ['Angola', 'AO']
    },
    'ARS': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Argentine peso',
		'countries': ['AR']
    },
    'AUD': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Australian dollar',
		'countries': ['AU']
    },
    'AWG': {
        'name': 'Aruban florin',
        SYMBOL: u'ƒ',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'countries': ['Aruba', 'AW']
    },
    'AZN': {
		SYMBOL: u'ман.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Azerbaijani manat',
        'countries': ['Azerbaijan', 'AZ']
    },
    'BAM': {
		SYMBOL: u'КМ',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Bosnia and Herzegovina convertible mark',
		'countries': ['BA', 'HR']
    },
    'BBD': {
        'name': 'Barbados dollar',
        SYMBOL: u'Bds$',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
        'countries': ['Barbados', 'BB']
    },
    'BDT': {
		SYMBOL: u'৳',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Bangladeshi taka',
		'countries': ['BD']
    },
    'BGN': {
		SYMBOL: u'лв',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Bulgarian lev',
		'countries': ['BG']
    },
    'BHD': {
		SYMBOL: u'د.ب.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Bahraini dinar',
        'countries': ['Bahrain', 'BH']
    },
    'BIF': {
        SYMBOL: u'FBu',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Burundian franc',
        'countries': ['Burundi', 'BI']
    },
    'BMD': {
        SYMBOL: u'BD$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Bermudian dollar',
        'countries': ['Bermuda', 'BM']
    },
    'BND': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Brunei dollar',
		'countries': ['BN']
    },
    'BOB': {
		SYMBOL: u'$b',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Boliviano',
		'countries': ['BO']
    },
    'BOV': {
#        SYMBOL: u'$',
        'name': 'Bolivian Mvdol (funds code)',
        'countries': ['Bolivia', 'BO']
    },
    'BRL': {
		SYMBOL: u'R$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Brazilian real',
		'countries': ['BR']
    },
    'BSD': {
        SYMBOL: u'B$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Bahamian dollar',
        'countries': ['Bahamas', 'BS']
    },
    'BTN': {
        SYMBOL: u'Nu.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Bhutanese ngultrum',
        'countries': ['Bhutan', 'BT']
    },
    'BWP': {
        SYMBOL: u'P',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Botswana pula',
        'countries': ['Botswana', 'BW']
    },
    'BYR': {
		SYMBOL: u'р.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Belarusian ruble',
		'countries': ['BY']
    },
    'BZD': {
		SYMBOL: u'BZ$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Belize dollar',
		'countries': ['BZ']
    },
    'CAD': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Canadian dollar',
		'countries': ['CA']
    },
    'CDF': {
        SYMBOL: u'FC',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Congolese franc',
        'countries': ['Democratic Republic of Congo', 'CD']
    },
    'CHF': {
		SYMBOL: u'SFr.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: '\'',
		GROUP_DIGITS: True,
		'name': 'Swiss franc',
		'countries': ['CH', 'LI']
    },

    'CLP': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Chilean peso',
		'countries': ['CL']
    },
    'CNY': {
		SYMBOL: u'¥',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Chinese yuan',
		'countries': ['CN', 'MN']
    },
    'COP': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Colombian peso',
		'countries': ['CO']
    },
    'CRC': {
		SYMBOL: u'₡',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Costa Rican colon',
		'countries': ['CR']
    },
    'CSD': {
        SYMBOL: u'Дин.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Serbian dinar',
		'countries': ['CS']
    },
    'CUC': {
#        SYMBOL: u'$',
        'name': 'Cuban convertible peso',
        'countries': ['Cuba']
    },
    'CUP': {
        SYMBOL: u'₱',
        'name': 'Cuban peso',
        'countries': ['Cuba']
    },
    'CVE': {
#        SYMBOL: u'$',
        'name': 'Cape Verde escudo',
        'countries': ['Cape Verde']
    },
    'CZK': {
		SYMBOL: u'Kč',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Czech koruna',
		'countries': ['CZ']
    },
    'DJF': {
#        SYMBOL: u'$',
        'name': 'Djiboutian franc',
        'countries': ['Djibouti']
    },
    'DKK': {
		SYMBOL: u'kr',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Danish krone',
		'countries': ['DK', 'FO', 'GL']
    },
    'DOP': {
		SYMBOL: u'RD$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Dominican peso',
		'countries': ['DO']
    },
    'DZD': {
		SYMBOL: u'د.ج.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Algerian dinar',
		'countries': ['DZ'],
    },
    'EEK': {
		SYMBOL: u'kr',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Estonia kroon',
		'countries': ['EE']
    },
    'EGP': {
		SYMBOL: u'ج.م.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Egyptian pound',
        'countries': ['Egypt', 'EG']
    },
    'ERN': {
#        SYMBOL: u'$',
        'name': 'Eritrean nakfa',
        'countries': ['Eritrea']
    },
    'ESP': {
		SYMBOL: u'₧',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Spanish peseta',
		'countries': ['ES']
    },
    'ETB': {
		SYMBOL: u'ETB',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'Ethiopian birr',
        'countries': ['Ethiopia', 'ET']
    },
    'EUR': {
        SYMBOL: u'€',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'Euro',
        'countries': ['17 European Union countries, Andorra, Kosovo, Monaco, Montenegro, San Marino, Vatican City; see eurozone', 'ES', 'FR', 'AT', 'DE', 'LU', 'GR', 'IE', 'FI', 'BE', 'NL', 'IT', 'PT', 'SK', 'LI', 'SI', 'ST']
    },
    'FJD': {
        SYMBOL: u'$',
        'name': 'Fiji dollar',
        'countries': ['Fiji', 'FJ']
    },
    'FKP': {
        SYMBOL: u'£',
        'name': 'Falkland Islands pound',
        'countries': ['Falkland Islands']
    },
    'GBP': {
		SYMBOL: u'£',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'Pound sterling',
        'countries': ['GB']
    },
    'GEL': {
		SYMBOL: u'Lari',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Georgian lari',
		'countries': ['GE']
    },
    'GHS': {
#        SYMBOL: u'₵',
        'name': 'Ghanaian cedi',
        'countries': ['Ghana']
    },
    'GIP': {
        SYMBOL: u'£',
        'name': 'Gibraltar pound',
        'countries': ['Gibraltar', 'GI']
    },
    'GMD': {
#        SYMBOL: u'$',
        'name': 'Gambian dalasi',
        'countries': ['Gambia', 'GM']
    },
    'GNF': {
#        SYMBOL: u'$',
        'name': 'Guinean franc',
        'countries': ['Guinea', 'GN']
    },
    'GTQ': {
		SYMBOL: u'Q',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Guatemalan quetzal',
		'countries': ['GT']
    },
    'GYD': {
        SYMBOL: u'$',
        'name': 'Guyanese dollar',
        'countries': ['Guyana', 'GY']
    },
    'HKD': {
		SYMBOL: u'HK$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Hong Kong dollar',
		'countries': ['HK']
    },
    'HNL': {
		SYMBOL: u'L.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Honduran lempira',
		'countries': ['HN']
    },
    'HRK': {
        SYMBOL: u'kn',
        'name': 'Croatian kuna',
        'countries': ['HR']
    },
    'HTG': {
#        SYMBOL: u'$',
        'name': 'Haitian gourde',
        'countries': ['Haiti', 'HT']
    },
    'HUF': {
		SYMBOL: u'Ft',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Hungarian forint',
		'coutries': ['HU']
    },
    'IDR': {
		SYMBOL: u'Rp',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Indonesian rupiah',
		'countries': ['ID']
    },
    'ILS': {
		SYMBOL: u'₪',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Israeli new sheqel',
		'countries': ['IL']
    },
    'INR': {
		SYMBOL: u'Rs.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Indian rupee',
		'countries': ['IN']
    },
    'IQD': {
		SYMBOL: u'د.ع.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'Iraqi dinar',
		'countries': ['IQ'],
    },
    'IRR': {
		SYMBOL: u'ريال',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '/',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Iranian rial',
        'countries': ['Iran', 'IR']
    },
    'ISK': {
		SYMBOL: u'kr.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': u'Icelandic króna',
		'countries': ['IS']
    },
    'JMD': {
		SYMBOL: u'J$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'Jamaican dollar',
        'countries': ['JM']
    },
    'JOD': {
		SYMBOL: u'د.ا.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Jordanian dinar',
		'countries': ['JO'],
    },
    'JPY': {
		SYMBOL: u'¥',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Japanese yen',
		'countries': ['JP']
    },
    'KES': {
		SYMBOL: u'S',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Kenyan shilling',
		'countries': ['KE']
    },
    'KGS': {
		SYMBOL: u'сом',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: '-',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Kyrgyzstani som',
		'countries': ['KG']
    },
    'KHR': {
		SYMBOL: u'៛',
		POSITIVE_FORMAT: u'{value}{symbol}',
		NEGATIVE_FORMAT: u'-{value}{symbol}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Cambodian riel',
        'countries': ['Cambodia', 'KH']
    },
    'KMF': {
        'name': 'Comoro franc',
#        SYMBOL: u'$',
        'countries': ['Comoros', 'KM']
    },
    'KPW': {
        'name': 'North Korean won',
        SYMBOL: u'₩',
        'countries': ['North Korea', 'KP']
    },
    'KRW': {
		SYMBOL: u'₩',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'South Korean won',
		'countries': ['KR']
    },
    'KWD': {
		SYMBOL: u'د.ك.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Kuwaiti dinar',
		'countries': ['KW'],
    },
    'KYD': {
        SYMBOL: u'$',
        'name': 'Cayman Islands dollar',
        'countries': ['Cayman Islands', 'KY']
    },
    'KZT': {
		SYMBOL: u'Т',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '-',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Kazakhstani tenge',
		'countries': ['KZ']
    },
    'LAK': {
		SYMBOL: u'₭',
		POSITIVE_FORMAT: u'{value}{symbol}',
		NEGATIVE_FORMAT: u'({value}{symbol})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Lao kip',
		'countries': ['LA']
    },
    'LBP': {
		SYMBOL: u'ل.ل.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Lebanese pound',
		'countries': ['LB']
    },
    'LKR': {
		SYMBOL: u'රු.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		 'name': 'Sri Lanka rupee',
		 'countries': ['LK']
    },
    'LRD': {
        SYMBOL: u'$',
        'name': 'Liberian dollar',
        'countries': ['Liberia', 'LR']
    },
    'LSL': {
#        SYMBOL: u'$',
        'name': 'Lesotho loti',
        'countries': ['Lesotho', 'LS']
    },
    'LTL': {
		SYMBOL: u'Lt',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Lithuanian litas',
		'countries': ['LT']
    },
    'LUF': {
        SYMBOL: u'F',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Luxembourg franc',
		'countries': ['LU']
    },
    'LVL': {
		SYMBOL: u'Ls',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'-{symbol} {value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Latvian lats',
		'countries': ['LV']
    },
    'LYD': {
		SYMBOL: u'د.ل.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Libyan dinar',
		'countries': ['LY']
    },
    'MAD': {
		SYMBOL: u'د.م.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Moroccan dirham',
		'countries': ['MA'],
    },
    'MDL': {
        'name': 'Moldovan le',
#        SYMBOL: u'$',
        'countries': ['Moldova (except Transnistria)', 'MD']
    },
    'MGA': {
#        SYMBOL: u'$',
        'name': 'Malagasy ariary',
        'countries': ['Madagascar', 'MG']
    },
    'MKD': {
		SYMBOL: u'ден.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Macedonian denar',
		'countries': ['MK']
    },
    'MMK': {
#        SYMBOL: u'$',
        'name': 'Myanma kyat',
        'countries': ['Myanmar', 'MM']
    },
    'MNT': {
		SYMBOL: u'₮',
		POSITIVE_FORMAT: u'{value}{symbol}',
		NEGATIVE_FORMAT: u'-{value}{symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Mongolian tugrik',
		'countries': ['MN']
    },
    'MOP': {
		SYMBOL: u'MOP',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Macanese pataca',
		'countries': ['MO']
    },
    'MRO': {
#        SYMBOL: u'$',
        'name': 'Mauritanian ouguiya',
        'countries': ['Mauritania', 'MR']
    },
    'MTL': {
        SYMBOL: u'Lm',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Maltese lira',
		'countries': ['MT']
    },
    'MUR': {
        SYMBOL: u'₨',
        'name': 'Mauritian rupee',
        'countries': ['Mauritius', 'MU']
    },
    'MVR': {
		SYMBOL: u'ރ.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'{value} {symbol}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Maldivian rufiyaa',
		'countries': ['MV']
    },
    'MWK': {
#        SYMBOL: u'$',
        'name': 'Malawian kwacha',
        'countries': ['Malawi', 'MW']
    },
    'MXN': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Mexican peso',
		'countries': ['MX']
    },
#    'MXV': {
#        'name': 'Mexican Unidad de Inversion (UDI) (funds code)',
#        SYMBOL: u'$',
#        'countries': ['Mexico']
#    },
    'MYR': {
		SYMBOL: u'RM',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Malaysian ringgit',
		'countries': ['MY']
    },
    'MZN': {
        SYMBOL: u'MT',
        'name': 'Mozambican metical',
        'countries': ['Mozambique', 'MZ']
    },
    'NAD': {
        SYMBOL: u'$',
        'name': 'Namibian dollar',
        'countries': ['Namibia', 'NA']
    },
    'NGN': {
        SYMBOL: u'₦',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Nigerian naira',
		'countries': ['NG']
    },
    'NIO': {
		SYMBOL: u'C$',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Cordoba oro',
		'countries': ['NI']
    },
    'NOK': {
		SYMBOL: u'kr',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Norwegian krone',
		'countries': ['NO']
    },
    'NPR': {
		SYMBOL: u'रु',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Nepalese rupee',
		'countries': ['NP']
    },
    'NZD': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
        'name': 'New Zealand dollar',
        'countries': ['NZ']
    },
    'OMR': {
        
		SYMBOL: u'ر.ع.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Omani rial',
        'countries': ['Oman', 'OM']
    },
    'PAB': {
		SYMBOL: u'B/.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Panamanian balboa',
		'countries': ['PA']
    },
    'PEN': {
		SYMBOL: u'S/.',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Peruvian nuevo sol',
		'countries': ['PE']
    },
    'PGK': {
#        SYMBOL: u'$',
        'name': 'Papua New Guinean kina',
        'countries': ['Papua New Guinea', 'PG']
    },
    'PHP': {
		SYMBOL: u'Php',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Philippine peso',
		'countries': ['PH']
    },
    'PKR': {
		SYMBOL: u'Rs',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Pakistani rupee',
		'countries': ['PK']
    },
    'PLN': {
		SYMBOL: u'zł',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': u'Polish złoty',
		'countries': ['PL']
    },
    'PYG': {
		SYMBOL: u'Gs',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': u'Paraguayan guaraní',
        'countries': ['Paraguay', 'PY']
    },
    'QAR': {
        
		SYMBOL: u'ر.ق.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Qatari rial',
		'countries': ['QA']
    },
    'RON': {
		SYMBOL: u'lei',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Romanian new le',
		'countries': ['RO']
    },
    'RSD': {
        SYMBOL: u'Дин.',
        'name': 'Serbian dinar',
        'countries': ['Serbia', 'CS']
    },
    'RUB': {
		SYMBOL: u'һ.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Russian rouble',
		'countries': ['RU']
    },
    'RWF': {
		SYMBOL: u'RWF',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Rwandan franc',
		'countries': ['RW']
    },
    'SAR': {
		SYMBOL: u'ر.س.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Saudi riyal',
		'countries': ['SA']
    },
    'SBD': {
        SYMBOL: u'$',
        'name': 'Solomon Islands dollar',
        'countries': ['Solomon Islands', 'SB']
    },
    'SCR': {
        SYMBOL: u'₨',
        'name': 'Seychelles rupee',
        'countries': ['Seychelles', 'SC']
    },
    'SDG': {
#        SYMBOL: u'$',
        'name': 'Sudanese pound',
        'countries': ['Sudan', 'SD']
    },
    'SEK': {
        SYMBOL: u'kr',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Swedish krona/kronor',
		'countries': ['SE']
    },
    'SGD': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Singapore dollar',
		'countries': ['SG']
    },
    'SHP': {
        SYMBOL: u'£',
        'name': 'Saint Helena pound',
        'countries': ['Saint Helena', 'SH']
    },
    'SLL': {
#        SYMBOL: u'$',
        'name': 'Sierra Leonean leone',
        'countries': ['Sierra Leone', 'SL']
    },
    'SOS': {
        SYMBOL: u'S',
        'name': 'Somali shilling',
        'countries': ['Somalia (except Somaliland)', 'SO']
    },
    'SRD': {
        SYMBOL: u'$',
        'name': 'Surinamese dollar',
        'countries': ['Suriname', 'SR']
    },
    'STD': {
#        SYMBOL: u'$',
        'name': u'São Tomé and Príncipe dobra',
        'countries': ['São Tomé and Príncipe', 'ST']
    },
    'SYP': {
		SYMBOL: u'ل.س.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Syrian pound',
		'countries': ['SY']
    },
    'SZL': {
#        SYMBOL: u'$',
        'name': 'Lilangeni',

        'countries': ['Swaziland', 'SZ']
    },
    'THB': {
		SYMBOL: u'฿',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Thai baht',
		'countries': ['TH']
    },
    'TJS': {
		SYMBOL: u'т.р.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ';',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Tajikistani somoni',
		'countries': ['TJ']
    },
    'TMT': {
		SYMBOL: u'm.',
		POSITIVE_FORMAT: u'{value}{symbol}',
		NEGATIVE_FORMAT: u'-{value}{symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Turkmenistani manat',
		'countries': ['TM']
    },
    'TND': {
		SYMBOL: u'د.ت.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Tunisian dinar',
		'countries': ['TN']
    },
    'TOP': {
#        SYMBOL: u'$',
        'name': u'Tongan paʻanga',
        'countries': ['Tonga', 'TO']
    },
    'TRY': {
		SYMBOL: u'TL',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Turkish lira',
		'countries': ['TR']
    },
    'TTD': {
		SYMBOL: u'TT$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Trinidad and Tobago dollar',
		'countries': ['TT']
    },
    'TWD': {
		SYMBOL: u'NT$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'-{symbol}{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'New Taiwan dollar',
		'countries': ['TW']
    },
    'TZS': {
#        SYMBOL: u'$',
        'name': 'Tanzanian shilling',
        'countries': ['Tanzania', 'TZ']
    },
    'UAH': {
		SYMBOL: u'грн.',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Ukrainian hryvnia',
		'countries': ['UA']
    },
    'UGX': {
#        SYMBOL: u'$',
        'name': 'Ugandan shilling',
        'countries': ['Uganda', 'UG']
    },
    'USD': {
		SYMBOL: u'$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'United States dollar',
		'countries': ['US', 'EC', 'PR', 'SV']
    },
    'UYU': {
		SYMBOL: u'$U',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'({symbol} {value})',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': 'Uruguayan peso',
		'countries': ['UY']
    },
    'UZS': {
		SYMBOL: u'сўм',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'Uzbekistan som',
        'countries': ['Uzbekistan', 'UZ']
    },
    'VEF': {
		SYMBOL: u'Bs',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol} -{value}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': u'Venezuelan bolívar fuerte',
		'countries': ['VE']
    },
    'VND': {
		SYMBOL: u'₫',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: '.',
		GROUP_DIGITS: True,
		'name': u'Vietnamese dong',
		'countries': ['VN']
    },
    'VUV': {
#        SYMBOL: u'$',
        'name': 'Vanuatu vat',
        'countries': ['Vanuat', 'VU']
    },
    'WST': {
#        SYMBOL: u'$',
        'name': 'Samoan tala',
        'countries': ['Samoa', 'WS']
    },
    'XAF': {
        SYMBOL: u'$',
        'name': 'CFA franc BEAC',
        'countries': ['Cameroon, Central African Republic, Republic of the Congo, Chad, Equatorial Guinea, Gabon', 'CM', 'CF', 'CG', 'TD', 'GQ', 'GA']
    },
    'XCD': {
        SYMBOL: u'$',
        'name': 'East Caribbean dollar',
        'countries': ['Anguilla, Antigua and Barbuda, Dominica, Grenada, Montserrat, Saint Kitts and Nevis, Saint Lucia, Saint Vincent and the Grenadines', 'AI', 'AG', 'DM', 'GD', 'MS', 'KN', 'LC', 'VC']
    },
    'XOF': {
		SYMBOL: u'XOF',
		POSITIVE_FORMAT: u'{value} {symbol}',
		NEGATIVE_FORMAT: u'-{value} {symbol}',
		DECIMAL_SYMBOL: ',',
		DIGIT_GROUP_SYMBOL: ' ',
		GROUP_DIGITS: True,
		'name': 'CFA Franc BCEAO',
        'countries': ["Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal, Togo", 'SN']
    },
    'XPF': {
#        SYMBOL: u'$',
        'name': 'CFP franc',
        'countries': ['French Polynesia, New Caledonia, Wallis and Futuna', 'PF', 'NC', 'WF']
    },
    'YER': {
		SYMBOL: u'ر.ي.‏',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}{value}-',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Yemeni rial',
        'countries': ['Yemen', 'YE']
    },
    'ZAR': {
		SYMBOL: u'R',
		POSITIVE_FORMAT: u'{symbol} {value}',
		NEGATIVE_FORMAT: u'{symbol}-{value}',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'South African rand',
		'countries': ['ZA']
    },
    'ZMK': {
#        SYMBOL: u'$',
        'name': 'Zambian kwacha',
        'countries': ['Zambia', 'ZM']
    },
    'ZWL': {
		SYMBOL: u'Z$',
		POSITIVE_FORMAT: u'{symbol}{value}',
		NEGATIVE_FORMAT: u'({symbol}{value})',
		DECIMAL_SYMBOL: '.',
		DIGIT_GROUP_SYMBOL: ',',
		GROUP_DIGITS: True,
		'name': 'Zimbabwe dollar',
		'countries': ['ZW']
    },
}
