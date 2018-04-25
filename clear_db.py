import models

models.db.drop_all()
models.db.create_all()

models.db.session.commit()
