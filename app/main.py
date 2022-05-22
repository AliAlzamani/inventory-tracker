import sqlite3
from flask import Flask,render_template, render_template_string,request,redirect,abort,flash
from app.models import db, ItemModel
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    try:
        if request.method == 'POST':
            item_id = request.form['item_id']
            discription = request.form['discription']
            quantity = request.form['quantity']
            manufacturer = request.form['manufacturer']
            item = ItemModel(item_id=item_id, discription=discription, quantity=quantity, manufacturer=manufacturer)
            db.session.add(item)
            db.session.commit()
            return redirect('/data')
    except:
        return redirect('/data')

 
@app.route('/', methods = ['GET','POST'])
def RetrieveList_initial():
    items = ItemModel.query.all()
    if request.method == 'GET':
        return render_template('datalist.html',items = items)
    if request.method == 'POST':
        return redirect('/data/create')


@app.route('/data', methods = ['GET','POST'])
def RetrieveList():
    items = ItemModel.query.all()
    if request.method == 'GET':
        return render_template('datalist.html',items = items)
    if request.method == 'POST':
        return redirect('/data/create')
 
 
@app.route('/data/<int:id>')
def Retrieveitem(id):
    item = ItemModel.query.filter_by(item_id=id).first()
    if item:
        return render_template('data.html', item = item)
    return f"item with id ={id} Doenst exist"
 
 
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    item = ItemModel.query.filter_by(item_id=id).first()
    if request.method == 'POST':
        if item:
            db.session.delete(item)
            db.session.commit()
            discription = request.form['discription']
            quantity = request.form['quantity']
            manufacturer = request.form['manufacturer']
            item = ItemModel(item_id=id, discription=discription, quantity=quantity, manufacturer = manufacturer)
            db.session.add(item)
            db.session.commit()
            return redirect(f'/data/{id}')
        return f"item with id = {id} Does nit exist"
 
    return render_template('update.html', item = item)
 
 
@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    item = ItemModel.query.filter_by(item_id=id).first()
    if request.method == 'POST':
        if item:
            db.session.delete(item)
            db.session.commit()
            return redirect('/data')
        abort(404)
 
    return render_template('delete.html')
