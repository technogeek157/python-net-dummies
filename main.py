global layer1, layer2, layer3, sWeights, input1, input2, sStarter
global inputs, layers, currPlayerMove, currNetMove, kpe

layer1 = ['i',]

layer2 = ['h','h']

layer3 = ['o']

layers = 3

input2 = []

while True:
  kpe = False
  
  currInput = raw_input("Choose: Collude or Backstab")
  if currInput.lower() == 'c':
    currPlayerMove = 0
    
  elif currInput.lower() == 'b':
    currPlayerMove = layer1
    
  else:
    print "Key Press Error, remember, only use c or b to indicate your move."
    kpe = True
    
  
