class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    
        if(len(image)<=sr or len(image[sr])<=sc ):
            return
        if(sr<0 or sc<0 ):
            return
        if(color==image[sr][sc]):
            return image
        
        pixel  = image[sr][sc]
        image[sr][sc] = color
        if((len(image)>sr and len(image[sr])-1>sc) and (image[sr][sc+1]==pixel)): 
           
            self.floodFill(image, sr, sc+1, color)#right
        
        if((len(image)>sr and sc>0) and (image[sr][sc-1]==pixel)): #left
            
            self.floodFill(image, sr, sc-1, color)

        if((len(image)-1>sr) and (image[sr+1][sc]==pixel)):        #dowm
            self.floodFill(image, sr+1, sc, color)

        if((sr>0) and (image[sr-1][sc]==pixel)):      #up
            self.floodFill(image, sr-1, sc, color)
        
       
        return image