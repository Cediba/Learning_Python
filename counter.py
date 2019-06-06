class Counter :
    ##Gets the current value of this counter
    #@return the current value
    #
    def get_value(self):
        return self._value
    ##Advance the value of this counter by 1   
    #
    def click(self):
        self._value = self._value + 1
    ##Resets the calue of this counter to 0
    # 
    def reset(self):
        self._value = 0