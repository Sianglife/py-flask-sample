from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

num_list = eval('[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118]')
mole_list = eval('["氫","氦","鋰","鈹","硼","碳","氮","氧","氟","氖","鈉","鎂","鋁","矽","磷","硫","氯","氬","鉀","鈣","鈧","鈦","釩","鉻","錳","鐵","鈷","鎳","銅","鋅","鎵","鍺","砷","硒","溴","氪","銣","鍶","釔","鋯","鈮","鉬","鎝","釕","銠","鈀","銀","鎘","銦","錫","銻","碲","碘","氙","銫","鋇","鑭","鈰","鐠","釹","鉕","釤","銪","釓","鋱","鏑","鈥","鉺","銩","鐿","鑥","鉿","鉭","鎢","錸","鋨","銥","鉑","金","汞","鉈","鉛","鉍","釙","砹","氡","鍅","鐳","錒","釷","鏷","鈾","錼","鈽","鋂","鋦","鉳","鉲","鑀","鐨","鍆","鍩","鐒","鑪","𨧀","𨭎","𨨏","𨭆","䥑","鐽","錀","鎶","鉨","鈇","鏌","鉝"]')
mole_dict = dict(zip(num_list, mole_list))
print(mole_dict)


@app.route('/mole/<num>', methods=['GET'])
def main(num):
    if request.method == 'GET':
        return render_template('form.html', num=num, name=mole_dict[int(num)])


@app.route('/mole/', methods=['POST'])
def mole():
    if request.method == 'POST':
        # print(request.form.to_dict())
        return redirect(url_for('main', num=request.form['num']))


if __name__ == '__main__':
    app.run()
