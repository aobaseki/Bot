import firebase_admin as admin
from firebase_admin import credentials
from firebase_admin import firestore
class Database(object):
    def __init__(self, ):
        self.cred = credentials.Certificate('path/to/serviceAccount.json')
        admin.initialize_app(self.cred)
        self.db = firestore.client()

    """ UPDATE DATA IN A FIELD """
    def set(self,collection,docid, data):
        doc_ref = self.db.collection(collection).document(docid)
        doc_ref.set(data, {"merge":True})
    
    """DELETE A SINGLE DOCUMENT"""
    def delete(self, collection, docid):
        doc = self.db.collection(collection).document(docid)
        doc.delete()

    """GET SINGLE DOCUMENT"""
    def get(self, collection, docid):
        doc = self.db.collection(collection).document(docid).get()
        # if found return a dictionary else false
        return doc.to_dict() if doc.exits else doc.exists


database = Database() 
        