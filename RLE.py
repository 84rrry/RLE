import re
class RLE:
    def encode(txt):
        rx = re.findall(r'((.)\2*)', txt)
        return ' '.join([f'{x[1]+str(len(x[0]))}' for x in rx])
    def decode(code,**args):

        #option to use a separator
        if 'separator' in args:
            separator=args['separator']
            rx=re.split(f'{separator}',code)
            return ''.join([f'{x[0]*int(x[1:])}' for x in rx])
        else:
           #don't use a seprator 
            rx=re.findall(r'.[0-9]+',code)
            return ''.join([f'{x[0]*int(x[1:])}' for x in rx])


