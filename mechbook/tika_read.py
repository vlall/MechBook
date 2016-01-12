# Tika 

import tika
from tika import parser
parsed = parser.from_file('out.txt')
metadata= parsed["metadata"]
content= parsed["content"]
print content
print metadata