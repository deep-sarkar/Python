class VendingMachine:
    def vending_machine(self, change):
        note = [1000,500,100,50,20,10,5,2,1]
        length = len(note)
        min_notes = 0
        index = 0
        while change != 0 and index < length:
            if change > note[index] :
                change = change - note[index]
                min_notes += 1
            else :
                index += 1
        return min_notes


