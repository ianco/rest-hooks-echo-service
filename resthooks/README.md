
Start a sjango shell and enter the following commands:

```bash
python manage.y shell

from django.contrib.auth.models import User
from rest_hooks.models import Hook
from tester.models import Book, Credential
import datetime

jrrtolkien = User.objects.create(username='jrrtolkien')

hook = Hook(user=jrrtolkien, event='book.added', target='http://localhost:8000/api/echo')
hook.save()     

book = Book(user=jrrtolkien, title='The Two Towers', pages=327, fiction=True)
book.save()   


jtolkien = User.objects.create(username='jtolkien')

hook = Hook(user=jtolkien, event='credential.added', target='http://localhost:8000/api/echo')
hook.save()     

cred = Credential(company_no = '123456', company_name = 'Ian Co', status = 'ACT', status_date = datetime.datetime.now())
cred.save()
```

