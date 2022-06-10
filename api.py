from flask import Flask,request
app=Flask(__name__)

@app.route('/')
def home():
    return "hello world"
@app.route('/iseven/<int:n>')
def iseven(n):
    if not n&1:
        return '{} is even'.format(n)
    else:
        return '{} is odd'.format(n)
@app.route('/isprime/<int:n>')
def isprime(n):
    if n==2 or n==3:
        return '{} is  prime'.format(n)
    if not n&1:
        return '{} is not prime'.format(n)
    if n%3==0:
        return '{} is not prime'.format(n)
    for i in range(5,int(n**(0.5))+1,6):
        if n%i==0:
            return '{} is not prime'.format(n)
    return '{} is  prime'.format(n)

if __name__=='__main__':
    app.run(debug=True)