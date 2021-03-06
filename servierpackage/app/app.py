
from keras.models import load_model
import numpy as np


from flask import (Flask, request, abort, jsonify, 
flash,  render_template)
from flask_cors import CORS

from rdkit.Chem import rdMolDescriptors, MolFromSmiles, rdmolfiles, rdmolops



def fingerprint_features(smile_string, radius=2, size=2048):
    mol = MolFromSmiles(smile_string)
    new_order = rdmolfiles.CanonicalRankAtoms(mol)
    mol = rdmolops.RenumberAtoms(mol, new_order)
    return rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius,
                                                          nBits=size,
                                                          useChirality=True,
                                                          useBondTypes=True,
                                                          useFeatures=False
                                                          )

  # create and configure the app
app = Flask(__name__)
#   setup_db(app)

# CORS(app)
#   STRING = '2076,3B,19C,138D,NULL,NULL'

# load model
model = load_model('../models/model1.h5')
  
@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def get_prediction():
    SMILE = request.form['text']
    SMILE = fingerprint_features(SMILE)
    SMILE = np.frombuffer(SMILE.ToBitString().encode(), 'u1') - ord('0')
    SMILE = SMILE.reshape((1, 2048))
    return 'The predection of P1 is:{}'.format(model.predict(SMILE))
      

def main():
    app.run(host='127.0.0.1', port=3001, debug=True)

if __name__ == '__main__':
    main()
    # app.run(host='127.0.0.1', port='12345', debug=True)
