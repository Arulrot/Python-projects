   
while True:
    lst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    option=input("Encode or Decode:").lower()
    word=input("Enter the word:").lower()
    shift=int(input("enter the shift key number:"))

    def encoding(word,shift):
        
        key=''
        for char in word:
            if char in lst:
                txt=lst.index(char)+shift
                txt%= len(lst)
                key+=lst[txt]
            else:
                key+=char
        print(f"\nYour Encoded Key is : {key}")

    def decoding(word,shift):
        
        key=''
        for char in word:
            if char in lst:
                txt=lst.index(char)-shift
                txt%= len(lst)
                key+=lst[txt]
            else:
                key+=char
        print(f"\nYour Decoded Key is : {key}")

    if option=="encode":
        encoding(word,shift)
    elif option=="decode":
        decoding(word,shift)
    else:
        print("\nYou have entered a wrong input")

    loop=input('\nDo you want to continue "Yes" or "No" :').lower()
    if loop=="yes":
        continue
    elif loop=="no":
        break
    else:
        break