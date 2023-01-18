f = open('aoc10.txt','rt')
raw_input = []
for line in f:
    raw_input += [line[:-1]]
f.close()

target_val1 = 17
target_val2 = 61
bots = {}
inputs = {}
outputs = {}
for line in raw_input:
    split_line = line.split(' ')
    if split_line[0] == 'value':
        chip_value = int(split_line[1])
        destination_name = split_line[-2]
        destination_number = split_line[-1]
        if destination_name == 'bot':
            if destination_number not in bots:
                bots[destination_number] = {'chips':[chip_value], 'low':[], 'high':[]}
            else:
                bots[destination_number]['chips'] += [chip_value]
        elif destination_name == 'output':
            if destination_number not in outputs:
                outputs[destination_number] = {'chips':[chip_value]}
            else:
                outputs[destination_number]['chips'] += [chip_value]
        elif destination_name == 'input':
            if destination_number not in inputs:
                inputs[destination_number] = {'chips':[chip_value]}
            else:
                inputs[destination_number]['chips'] += [chip_value]
    else:
        directed_bot = split_line[1]
        low_recipient = [split_line[5], split_line[6]]
        high_recipient = [split_line[10], split_line[11]]
        if directed_bot not in bots:
            bots[directed_bot] = {'low':low_recipient, 'high': high_recipient, 'chips':[]}
        else:
            bots[directed_bot]['low'] = low_recipient
            bots[directed_bot]['high'] = high_recipient
# Now start to loop through
bots_trading = True
target_bot = ''
while bots_trading == True:
    bots_trading = False
    for bot in bots:
        
        if len(bots[bot]['chips']) == 2:
            # need to trade
            low_value = min(bots[bot]['chips'])
            high_value = max(bots[bot]['chips'])
            if (low_value == target_val1) and (high_value == target_val2):
                target_bot = bot
            low_recipient = bots[bot]['low']
            high_recipient = bots[bot]['high']
            # check low recipient
            can_trade = True
            if low_recipient[0] != 'output':
                if len(bots[low_recipient[1]]['chips']) >= 2:
                    can_trade = False
            if high_recipient[0] != 'output':
                if len(bots[high_recipient[1]]['chips']) >= 2:
                    can_trade = False
            if can_trade == True:
                bots_trading = True
                bots[bot]['chips'] = []
                if low_recipient[0] == 'output':
                    if low_recipient[1] not in outputs:
                        outputs[low_recipient[1]] = {'chips':[low_value]}
                    else:
                        outputs[low_recipient[1]]['chips'] += [low_value]
                else:
                    bots[low_recipient[1]]['chips'] += [low_value]
                if high_recipient[0] == 'output':
                    if high_recipient[1] not in outputs:
                        outputs[high_recipient[1]] = {'chips':[high_value]}
                    else:
                        outputs[high_recipient[1]]['chips'] += [high_value]
                else:
                    bots[high_recipient[1]]['chips'] += [high_value]
print('Part 1: bot ' + target_bot + ' is responsible for comparing chips ' + str(target_val1) + ' and ' + str(target_val2))
chip0 = outputs['0']['chips'][0]
chip1 = outputs['1']['chips'][0]
chip2 = outputs['2']['chips'][0]
print('Part 2: multiplying one chip from outputs 0, 1, and 2 yields ' + str(chip0 * chip1 * chip2))