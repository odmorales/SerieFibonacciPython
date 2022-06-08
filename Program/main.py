from serieFibonacci import Serie

def main(): 
    serie = Serie()
    print(serie.getSerie(10))
    
if __name__ == '__main__':
    import sys
    sys.exit(int(main() or 0))