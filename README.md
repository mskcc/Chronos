# Chronos

Code to generate time based UUID's that sort properly (chronologically). The code generates
proper `uuid.UUID` objects that are drop in replacements for `uuid.uuid4`.


##Example

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

## Test script:

```{bash}
python3 testTemporalUUID.py 5
11eaac5f-e3a5-0114-90e6-97fe45bfc964
11eaac5f-e3a5-0466-b33c-a8c893766824
11eaac5f-e3a5-0524-b99a-c10f538a446f
11eaac5f-e3a5-05c4-8c16-9db245df9a50
11eaac5f-e3a5-0650-9f87-911aaaafe7f2
```

## Format Specification

The first 8 bytes are taken from the first 8 bytes of a time based uuid `uuid.uuid1()` but units are reversed to _normal_ human order of MSB to LSB (not f#cking stupid LSB->MSB order). In detail if:

```
uuid1Str == "AAAABBBB-CCCC-DDDD"
```

then the natural order would be

```
uuidTStr == "DDDDCCCC-AAAA-BBBB"
```

This will guarentee that when sorted they will sort chronologically.

The last 8 bytes come from the last 8 bytes random uuid `uuid.uuid()`. This will prevent collisions no matter how fast you generate them or if you generate then simultaneously on different processes.

```
uuidTStr == "DDDDCCCC-AAAA-BBBB-RRRR-SSSSSSSS"
             ^^==---- ==== --^^ =============
             MSB            LSB  Random UUID
```

With 8 bytes of randomness you would need to generate ` ~ 2^(4*8) ~ 4e9` uuid's in the smallest time resolution of your computer which is likely less than a microsec to have a 50% chance of a collision. And at nanosecond resolution you would have rollover in `~500` years.




