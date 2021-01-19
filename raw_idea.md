# Rough idea canvas

In 1 : Plot x and y data points

Out 1 : 

**snippets**: 

    { import matplotlib.pyplot as plt
      plt.plot(x,y) }
                
**variables**: x , y , marker, color, more...

**suggested additions**: Add x, y labels with 

    { plt.xlabel('Insert label text')                                               
      plt.ylabel('Insert label text') }
                                                
In 2 : Fit data points with line

Out 2 :

**snippets**: 

    {plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x))) Comment : "Using np.unique(x) instead of x handles the case where x isn't sorted or has duplicate values."}

**variables**: x , y , degree, more...


