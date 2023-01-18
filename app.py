from flask import Flask,render_template,request,redirect
import sqlite3 as sql
import templates

app=Flask("__name__")




@app.route("/",methods=['POST','GET'])
def fun():
    if request.form.get('video1')!=None:
        conn=sql.connect('url.db')
        video1=request.form.get('video1')
        image1=request.form.get('image1') 
        cur=conn.cursor()
        cur.execute('insert into connect (video1,image1) values(?,?)',(video1,image1))
        conn.commit()
    return render_template("data.html")


@app.route('/view',methods=['POST','GET'])
def select():
    conn=sql.connect('url.db')
    cur=conn.cursor()
    cur.execute("Select * from connect")
    row=cur.fetchall()
    a=[]
    b=[]
    for i in row:
        a.append(i[0])
        b.append(i[1])
    print(a,b)
    return render_template("videoplayer.html",data=a,data1=b)

@app.route('/view1',methods=['POST','GET'])
def select1():
    conn=sql.connect('url.db')
    cur=conn.cursor()
    cur.execute("Select * from connect")
    row=cur.fetchall()
    a=[]
    b=[]
    for i in row:
        a.append(i[0])
        b.append(i[1])
    print(a,b)
    return render_template("index.html",data=a,data1=b)



if __name__=="__main__":
    app.run(debug=True)