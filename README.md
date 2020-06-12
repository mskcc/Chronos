# Chronos

Code to generate time based UUID's that sort properly (chronologically)

How to use, if you have code that looks like this:

```{python}
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

def test_create_file_obj_bad_file_group(self):
        file_group_id = str(uuid.uuid4())

```

then change it to:

```{python}
import chronos

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=chronos.uuidT, editable=False)

def test_create_file_obj_bad_file_group(self):
        file_group_id = str(chronos.uuidT())

```

