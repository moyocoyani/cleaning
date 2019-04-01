# Ensure to make lowers the text. Remove punctuations and accent marks.

def textNormalizer(dataset,attribute):
    #Devuelve el texto sin acentos y minúsculas.
    return dataset[attribute].str.lower().str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
