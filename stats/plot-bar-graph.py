import matplotlib.pyplot as plt 

class PlotBarGraph:
    '''
        data_x x-axis data []
        data_y y-axis data []
        label_x label for x axis
        label_y label for y axis
    '''
    def __init__(self, data_x, data_y, label_x = "x-axis", label_y = "y-axis", title = "Graph"):
        self.data_x = data_x
        self.data_y = data_y
        self.label_x = label_x
        self.label_y = label_y
        self.title = title

    #Execute
    def run(self):
        # plotting the points  
        plt.plot(self.data_x, self.data_y) 
        # naming the x axis 
        plt.xlabel(self.label_x) 
        # naming the y axis 
        plt.ylabel(self.label_y)  
        # giving a title to my graph 
        plt.title(self.title) 
        # function to show the plot 
        plt.show() 
