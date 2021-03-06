
def caesar_cipher(message, shift, cipher_direction):
  result_message=''
  # Make the shift negative if the use wants to decode. 
  if cipher_direction=='decode':
    shift*=-1
  for char in message:
    # if character is uppercase use the ASCII represetation of uppercase letter i.e From 65-90
    # ord converts string to ASCII 
    # chr coverts ASCII to string
    if char.isupper():
      # Calculate shift amount, ASCII value of Character + Shift - ASCII value of A(65)
      # shift_ammount%26 ensures that the shift amount value lies between 0-26
      shift_amount=ord(char)+shift-65
      result_message+=chr(shift_amount%26+65)
    elif char.isspace() or char.isdigit():
      result_message+=char
    else:
      result_message+=chr((ord(char)+shift-97)%26+97)
  print(f'{cipher_direction}d message:{result_message}')

end=False
while not end:
  direction=input('Type encode to encrypt your message and decode to decrypt:\n')
  message=input('Enter your message: ')
  shift=int(input('Enter Shift number: '))
  caesar_cipher(message, shift, direction)

  run_again=input('Do you want to go again? Type yes or no\n').lower()
  
  if run_again=='no':
    end=True
