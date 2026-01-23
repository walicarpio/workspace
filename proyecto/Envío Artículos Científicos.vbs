Set WshShell = CreateObject("WScript.Shell")

' Ejemplo de ruta: "C:\Users\Admin\AppData\Local\Programs\Python\Python311\Scripts\streamlit.exe"
Dim exePath
exePath = "C:\Users\eberrios\AppData\Local\Programs\Python\Python314\python.exe\Scripts\streamlit.exe"

' Ejecutamos: streamlit run app.py
WshShell.Run "cmd.exe /c " & Chr(34) & exePath & Chr(34) & " run app.py", 0

Set WshShell = Nothing