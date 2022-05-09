public class Solution {
    public int[][] FloodFill(int[][] image, int sr, int sc, int newColor) {
        Dictionary<string, int> visited = new Dictionary<string, int>();
        FloodFillHelper(image, sr, sc, image[sr][sc], newColor, visited);
        return image;
    }
    
    
    public void FloodFillHelper(int[][] image, int sr, int sc, int originalColor, int newColor, Dictionary<string, int> visited){
        
        string currKey = sr.ToString()+ sc.ToString();
        if(visited.ContainsKey(currKey)) {
            return;
        }
        visited.Add(currKey, 1);
        
        image[sr][sc] = newColor;
        
        //check bottom
        if ( sr-1 >=0 && image[sr-1][sc] == originalColor){
            FloodFillHelper(image, sr-1, sc, originalColor, newColor, visited);
        }
        
        
        //check top
         if ( sr+1 < image.GetLength(0) && image[sr+1][sc] == originalColor){
            FloodFillHelper(image, sr+1, sc, originalColor, newColor, visited);
        }
        
        //check left
         if ( sc-1 >=0 && image[sr][sc-1] == originalColor){
            FloodFillHelper(image, sr, sc-1, originalColor, newColor, visited);
        }
        
        //check right
         if ( sc+1 < image[0].GetLength(0) && image[sr][sc+1] == originalColor){
            FloodFillHelper(image, sr, sc+1, originalColor, newColor, visited);
        }
        
    }
    
    
}