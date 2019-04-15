from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import date
from flask import request
from flask import jsonify


app = Flask(__name__)
myDatabase = 'dertliler.db'

@app.route('/')
def index():
	conn = sqlite3.connect(myDatabase)
	c = conn.cursor()
	c.execute('select * from data')
	result = c.fetchall()

	return render_template('index.html', icerik=result)


@app.route('/ekle', methods=['POST'])
def ekle():
	entryNo = request.form['entryNo']
	
	#burda asagidaki check e ip de ekleyip eger ip ayniysa direk yazmayiz
	ip_addr = request.remote_addr
	print ip_addr


	#once check edelim var mi
	conn = sqlite3.connect(myDatabase)
	c = conn.cursor()
	c.execute('select * from data where entry_no = ?', [entryNo])
	result = list(c.fetchall())
	result = map(lambda x:list(x), result)
	for record in result:
		if (record[1]):
			if(record[3]):
				print 'bu ip kayit yapmis'
				return redirect(url_for('index'))
			else:
				dert = int(record[2])
				dert = dert + 1
				c.execute('update data set dert = ? where entry_no = ?', (dert, entryNo))
				conn.commit()
				return redirect(url_for('index'))
	dert = 1
	c.execute('insert into data(entry_no, dert, ip) values(?,?,?)', (entryNo, dert, ip_addr))
	conn.commit()
	return redirect(url_for('index'))

if __name__ == "__main__":
	app.run(debug=True)