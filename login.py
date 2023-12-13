
from tkinter import *
from tkinter import ttk

# tkinter 객체 생성
window = Tk()
window.title("Login")

#사용자 id와 password를 저장
user_id, password = StringVar(), StringVar()

# 사용자 id와 password를 비교
def check_data():
    if user_id.get() == "Open_Source" and password.get() == "programming":
        print("Logged IN Successfully")
    else:
        print("Check your Usernam/Password")

# id와 password, 그리고 확인 버튼의 UI 생성
ttk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
ttk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
ttk.Entry(window, textvariable = user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
ttk.Entry(window, textvariable = password, show='*').grid(row = 1, column = 1, padx = 10, pady = 10)
ttk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()
