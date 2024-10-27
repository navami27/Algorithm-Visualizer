import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sorting_algorithms import BubbleSort,MergeSort,QuickSort,InsertionSort,ShellSort,cycleSort,timSort,cocktail_sort
import sys
import random
import pygame
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.load("C:/path/to/music file")  # Replace "your_music_file.mp3" with the path to your music file
    pygame.mixer.music.play(-1)    
if __name__=='__main__':
    ms_speed=350
    li=[]
    step_cnt=0
    
    try:
        N=int(input("Enter no of elements to be sorted:"))
        choice=int(input("Choice(1:select randomly,2:input manually): "))
        if choice==1:
            li=random.sample(range(0,2*N),N)
        elif choice==2:
            for i in range(N):
                num=input("Enter {}th element: ".format(i+1))
                li.append(int(num))
        else:
            sys.exit("Invalid input")
        algo_dict={1:'Bubble Sort',2:'Merge Sort',3:'Insertion Sort',4:'Shell sort',5:'Quick Sort',6:'Cycle Sort',7:'Tim Sort',8:'Cocktail Sort'}
        algo=int(input("Choose sorting algorithm:\n{}: ".format(algo_dict)))
        if algo==1:
            generator_func=BubbleSort(li)
        elif algo==2:
            generator_func=MergeSort(li,0,N-1)
        elif algo==3:
            generator_func=InsertionSort(li)
        elif algo==4:
            generator_func=ShellSort(li)
        elif algo==5:
            generator_func=QuickSort(li,0,N-1)
        elif algo==6:
            generator_func=cycleSort(li)
        elif algo==7:
            generator_func=timSort(li)
        elif algo==8:
            generator_func=cocktail_sort(li)
        else:
            sys.exit("Invalid input")
    except Exception as e:
        raise e
    
fig, ax = plt.subplots(num= 'Sorting Algorithm Visualizer')
ax.set_title(algo_dict[algo])
plt.xlabel('Elements being sorted')
bar_rec = ax.bar(range(len(li)), li, tick_label=li)
cmap = plt.cm.get_cmap('viridis', len(li))  # Choose a colormap
colors = [cmap(i) for i in range(len(li))]  # Assign colors based on the colormap

    # Apply colors to bars
for rect, color in zip(bar_rec, colors):
    
    
    rect.set_color(color)#container for bar diagram.
    # by using plt.gcf().transFigure, (0,0) is the bottom left and (1,1) is the top right of the figure
plt.text(0.015, 0.94, 'input:{}'.format(str(li)), fontsize=10, transform=plt.gcf().transFigure) #to show input data
step_text = plt.text(0.015, 0.90, "", fontsize=10, transform=plt.gcf().transFigure)
play_music()#to show no. steps

def update_fig(li):
    global step_cnt
    for rect,val in zip(bar_rec,li):
        rect.set_height(val)
        ax.set_xticklabels(li)
    step_cnt+=1
    step_text.set_text('No. of steps: {}'.format(step_cnt))
def end_animation(_):
        # Stop music playback when animation ends
        pygame.mixer.music.stop()    
anim=animation.FuncAnimation(fig,func=update_fig,frames=generator_func,interval=ms_speed,repeat=False)
plt.show()    
    
    
        
                

