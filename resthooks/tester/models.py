from django.db import models

# Create your models here.

class Book(models.Model):
    # NOTE: it is important to have a user property
    # as we use it to help find and trigger each Hook
    # which is specific to users. If you want a Hook to
    # be triggered for all users, add '+' to built-in Hooks
    # or pass user_override=False for custom_hook events
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # maybe user is off a related object, so try...
    # user = property(lambda self: self.intermediary.user)

    title = models.CharField(max_length=128)
    pages = models.PositiveIntegerField()
    fiction = models.BooleanField()

    # ... other fields here ...

    def serialize_hook(self, hook):
        # optional, there are serialization defaults
        # we recommend always sending the Hook
        # metadata along for the ride as well
        return {
            'hook': hook.dict(),
            'user': {'username': hook.user.username},
            'data': {
                'id': self.id,
                'title': self.title,
                'pages': self.pages,
                'fiction': self.fiction,
                # ... other fields here ...
            }
        }

    def mark_as_read(self):
        # models can also have custom defined events
        from rest_hooks.signals import hook_event
        hook_event.send(
            sender=self.__class__,
            action='read',
            instance=self # the Book object
        )


class Credential(models.Model):
    company_no = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    status_date = models.DateField()

    # ... other fields here ...

    def serialize_hook(self, hook):
        # optional, there are serialization defaults
        # we recommend always sending the Hook
        # metadata along for the ride as well
        return {
            'hook': hook.dict(),
            'user': {'username': hook.user.username},
            'data': {
                'id': self.id,
                'company_no': self.company_no,
                'company_name': self.company_name,
                'status': self.status,
                'status_date': self.status_date,
                # ... other fields here ...
            }
        }
