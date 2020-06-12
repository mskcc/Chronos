# Chronos

Code to generate time based UUID's that sort properly (chronologically)

How to use, if you have code that looks like this:

```{python}
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
```

then change it to:

```{python}
import genTemporalUUID

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=genTemporalUUID.genTemporalUUID, editable=False)
```

