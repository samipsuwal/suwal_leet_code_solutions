public class Logger {
    private Dictionary<string, int> dict;

    public Logger() {
        this.dict = new Dictionary<string, int>();
    }
    
    public bool ShouldPrintMessage(int timestamp, string message) {
        // Check if message exists in Dictionary
        
        if (!this.dict.ContainsKey(message)){
            dict.Add(message, timestamp + 10);
            return true;
        } 
        else {
            if (timestamp >= dict[message]){
                dict[message] = timestamp+ 10;
                return true;
            }
            return false;
        }
    }
}

/**
 * Your Logger object will be instantiated and called as such:
 * Logger obj = new Logger();
 * bool param_1 = obj.ShouldPrintMessage(timestamp,message);
 */