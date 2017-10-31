global layer1, layer2, layer3, layer4

global input1, input2, input3, input4, input5, input6
#for lastmove player, lastmove net, history player, history net
#score player, and score net

global inputs, layers, currPlayerMove, currNetMove, kpe

global playerHistory, netHistory, lastPlayerMove, lastCompMove, sStarter

global layer1W, layer2W, layer3W, layer4W


layer1 = [0]#these are for neurons per layer, i for input, h for hidden, o for output
layer2 = [0]
layer3 = [0]
layer4 = [0]

layer1W = []

sStarter = 1 #starting weights

i = 0
while i < len(layer1):
  layer1W.append(sStarter)
  i = i + 1
  
i = 0
while i 

print layer1W

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

    