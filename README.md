```shell
docker compose up -d
pip install psycopg2-binary
python insert_data.py
python select_data.py
```

## Produces

```shell
❯ python select_data.py
UTC Date Count for CURRENT_DATE: 10
Count for CURRENT_DATE on timezone -8: 1
```
