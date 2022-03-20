from firebase_admin import credentials, initialize_app, storage

cred = credentials.Certificate('service_account_key.json')
initialize_app(cred, {'storageBucket': 'cost-estimation-aed7d.appspot.com'})

def upload_usecase(filepath):
    bucket = storage.bucket()
    blob = bucket.blob(filepath)
    blob.upload_from_filename(filepath)
    blob.make_public()
    return blob.public_url