# Impor
from flask import Flask, render_template, request


app = Flask(__name__)

#def result_calculate(size, lights, device):
    # Variabel yang memungkinkan penghitungan konsumsi energi peralatan
    #home_coef = 100
    #light_coef = 0.04
    #devices_coef = 5   
    #return size * home_coef + lights * light_coef + device * devices_coef 

# Halaman pertama
@app.route('/')
def index():
    return render_template('index.html')
# Halaman kedua
@app.route('/<size>')
def lights(size):
    return render_template(
                           'lights.html', 
                            size=size
                           )


@app.route('/test/<sieze>')
def bothz(sieze):
    return render_template(
                           'mist.html', 
                            size=sieze
                           )

# Halaman ketiga
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                           size = size, 
                            lights = lights                           
    )

@app.route('/test/<sieze>/<lit>')
def elect(sieze, lit):
    return render_template(
                            'gotta.html',                           
                           size = sieze, 
                            lights = lit  
    )
# Perhitungan
#@app.route('/<size>/<lights>/<device>')
#def end(size, lights, device):
    #return render_template('end.html', 
                            #result=result_calculate(int(size),
                                                    #int(lights), 
                                                    #int(device)
#                                                    )
#                        )
# Formulir
@app.route('/form')
def form():
    return render_template('form.html')

#Hasil formulir
@app.route('/submit', methods=['POST'])
def submit_form():
    # Mendeklarasikan variabel untuk pengumpulan data
    name = request.form['name']

    # Anda dapat menyimpan data Anda atau mengirimkannya melalui email
    return render_template('form_result.html', 
                           # Tempatkan variabel di sini
                           name=name,
                           )

app.run(debug=True)
