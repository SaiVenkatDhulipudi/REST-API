from flask import Flask,request,jsonify
app=Flask(__name__)

helper=dict()
helper["iseven/int"]="returns if a number is even or not"
helper["isprime/int"]="returns if a number is prime or not"

@app.route('/')
def home():
    return jsonify(helper) 

@app.route('/iseven/<int:n>' methods=["POST"])
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
@app.route('/ispalindrome/<int:n>')
def ispali(n):
    c=0
    k=n
    while k:
        c=c*10
        c+=k%10
        k=k//10
    if c==n:
        return "{} is palindrome".format(n)
    else:
        return "{} is not palindrome".format(n)

if __name__=='__main__':
    app.run(debug=True)