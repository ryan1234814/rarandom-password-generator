import string
import tkinter as tk
from tkinter import messagebox,scrolledtext,simpledialog,filedialog
import random
class PasswordGeneratorApp:
    def __init__(self,master):
        self.master=master #represents the main window of application which is passed when an instance od=f class is created
        self.master.title("Password Generator")
        self.password_history=[]#initialize the list to store history of generated passwords
        self.create_widgets()#call create_widget method responsible for creating and arranging user interface elements in main window
    def create_widgets(self):
            self.length_label=tk.Label(self.master,text="Password Length")
            self.length_label.pack(pady=5)#adds a label to window and apply verical padding of 5px
            self.length_entry=tk.Entry(self.master)#create an empty widget to the window with vertical padding
            self.length_entry.pack(pady=5)
            self.length_entry.insert(0,"11")#indicate default password length
            #track whether uppercase letters should be included in password
            self.include_uppercase=tk.BooleanVar(value=True)
            #inclusion of lowercase letters
            self.include_lowercase=tk.BooleanVar(value=True)
            #inclusion of digits
            self.include_digits=tk.BooleanVar(value=True)
            #include special characters
            self.include_special=tk.BooleanVar(value=True)
            #create checkboxes for creating password
            tk.Checkbutton(self.master,text="Include Uppercase letters",variable=self.include_uppercase).pack()
            tk.Checkbutton(self.master,text="Include Lowercase letters",variable=self.include_lowercase).pack()
            tk.Checkbutton(self.master,text="Include Digits",variable=self.include_digits).pack()
            tk.Checkbutton(self.master,text="Include special characters",variable=self.include_special).pack()
            #creates a button"generate password" when clicked it shows show_password method to generate and display the password
            self.generate_button=tk.Button(self.master,text="Generate password",command=self.show_password)
            self.generate_button.pack(pady=10)
            #create a button called "save password"
            #when clicked it calls save_password method to svae the password generated in the file
            self.save_button=tk.Button(self.master,text="Save password",command=self.save_password)
            self.save_button.pack(pady=10)
            #create a button to show password history.
            #when clicked it shows  show_history which contains the list of random passwords used
            self.history_button=tk.Button(self.master,text="Show password history",command=self.show_history)
            self.history_button.pack(pady=10)
    def generate_password(self):
         #defines the method which generates password based on iser's preferences
         #retrieves the password length entered by user in the entry widget and converts to integer
            length=int(self.length_entry.get())
         #to build set of characters to be included in the password
            characters=""
            if self.include_uppercase.get():#contains all uppercase letters
                characters+=string.ascii_uppercase
            if self.include_lowercase.get():#contains all lowercase letters
                  characters+=string.ascii_lowercase
            if self.include_digits.get():#contains all digits
                  characters+=string.digits
            if self.include_special.get():#contains all special characters
                  characters+=string.punctuation  
            #check if the character string is empty      
            if not characters:
                  messagebox.showwarning("please select at least one character type")
                  return None
            #generates a random password by selecting random characters from the characters string
            password = ''.join(random.choice(characters) for _ in range(length))
            return password
    def show_password(self):
          #display the generated password in a message box
            #creates a new password
            password=self.generate_password()
            #if password was successfully generated it is then appended to password_history list
            if password:
                  self.password_history.append(password)
                  messagebox.showinfo("Generated password",f"Your password is:{password}")
    def save_password(self):
          #to create a new password for saving
          password=self.generate_password()         
          if password:
                #opens a file save dialog
                #allowing users to choose where to save the password
                
                file_path=filedialog.asksaveasfile(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")])     
                #if user selected a file-path it opens the specified file_name
                #in write mode and writes the generated password to it
                if file_path:
                      with open(file_path,'w') as file:
                            file.write(password)
                      messagebox.showinfo("Success", "Pssword was saved successfully")
    def show_history(self):
        #creates history window for displaying password history
        history_window=tk.Toplevel(self.master)
        history_window.title("Password History")  
        #create a scrollable text area in history window
        #this allows users to view multiple lines of text
        history_text=scrolledtext.ScrolledText(history_window,width=40,height=10)
        history_text.pack(pady=10)
        #if there are any passwords in the password_history
        #if yes it joins them into a single string with line breaks and inserts them into text area
        if self.password_history:
              history_text.insert(tk.END, "\n".join(self.password_history))
        #if it is empty it displays no messages created      
        else:
              history_text.insert(tk.END, "No passwords generated yet.")    
        #sets the text area to a read only state 
        # #prevent users from editing the displayed text      
        history_text.config(state=tk.DISABLED)       
# Create the main window
root = tk.Tk()
app = PasswordGeneratorApp(root)  
# Run the application
root.mainloop()      





          
            


