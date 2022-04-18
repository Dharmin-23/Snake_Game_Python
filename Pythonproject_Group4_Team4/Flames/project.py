from tkinter import *
def rem_mat_char(lst1, lst2):  # function helps to remove one of the common character present in lst1 and lst2 if present
	for i in range(len(lst1)) : 
		for j in range(len(lst2)) : 
			if lst1[i] == lst2[j] : 
				c = lst1[i]    # c is one of the common character of lst1 and lst2 
				lst1.remove(c) #remove common character from both lst1 and lst2 
				lst2.remove(c) 
				lst3 = lst1 + ["*"] + lst2  # here "*" is used between lst1 and lst2 which helps to extract lst1 and extract lst2 after returning lst3
				return [lst3, True]  
	lst3 = lst1 + ["*"] + lst2 
	return [lst3, False] 
def status_output() :  
	p1 = Player1.get() 
	p1 = p1.lower()  
	p1.replace(" ", "")  # remove spaces between words (entered input names may contain space) 
	p1_lst = list(p1)    # making list from string
	p2 = Player2.get() 
	p2 = p2.lower() 
	p2.replace(" ", "") 
	p2_lst = list(p2)  
	bol = True
	while bol :  
		return_lst = rem_mat_char(p1_lst, p2_lst) 
		con_list = return_lst[0] 
		bol = return_lst[1]  
		index = con_list.index("*")   
		p1_lst = con_list[ : index]  # slicing returned list into p1_lst and p2_lst
		p2_lst = con_list[index + 1 : ] 
	count = len(p1_lst) + len(p2_lst) 
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]  
	while len(result) > 1 :  
		split_index = (count % len(result) - 1)  
		if split_index >= 0 : 
			result.pop(split_index) 
		else : 
			result.pop(-1)
	Status.insert(9, result[0])
 
def clear_all() : # delete the content present in entry widgit of player1 Name,player2 Name,Relationship status
	Player1.delete(0, END) 
	Player2.delete(0, END) 
	Status.delete(0, END) 
	Player1.focus_set() # points the cursor to player1 Name entry widget

if __name__ == "__main__" : 
	screen = Tk()  # is used to create main window of the apllication
	screen.configure(background = 'gold') 
	screen.geometry("350x150")    # here the argument is "width x height"
	screen.title("Flames Game") 
	label1 = Label(screen, text = "Player 1 Name: ", 
				fg = 'black', bg = 'white')   # bg=background fg=foreground
	label2 = Label(screen, text = "Player 2 Name: ", 
				fg = 'black', bg = 'white')   
	label3 = Label(screen, text = "Relationship Status: ", 
				fg = 'black', bg = 'white') 
        #grid is used to place widgets according to mentioned row and column inside it
	label1.grid(row = 1, column = 0, sticky ="E")  #sticky(compass direction indicating the sides and corners of the cell to which widget sticks)
	label2.grid(row = 2, column = 0, sticky ="E")  # here 'E' in sticky used to indicate compass direction "east"
	label3.grid(row = 4, column = 0, sticky ="E") 
	Player1 = Entry(screen)    #used to accept single line text strings from user
	Player2 = Entry(screen) 
	Status = Entry(screen)
	Player1.grid(row = 1, column = 1, ipadx ="50")   #ipadx(how many pixels to pad widget horizontally inside the widgets border)
	Player2.grid(row = 2, column = 1, ipadx ="50") 
	Status.grid(row = 4, column = 1, ipadx ="50") 
	button1 = Button(screen, text = "Submit", bg = "green", 
					fg = "black", command = status_output)   # here command is excetuted when button clicked event happened
	button2 = Button(screen, text = "Clear", bg = "green", 
					fg = "black", command = clear_all)
	button1.grid(row = 3, column = 1) 
	button2.grid(row = 5, column = 1)
	screen.mainloop() #tells python to run tkinter event loop
