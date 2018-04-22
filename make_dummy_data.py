import models

models.db.drop_all()
models.db.create_all()

for i in range(100):
	cred = models.FacebookCredential(username=f'user{i}', password=f'pass{i}')
	models.db.session.add(cred)

models.db.session.commit()
