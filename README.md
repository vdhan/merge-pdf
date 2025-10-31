# Hợp nhất file PDF
## Cài đặt
Tạo môi trường:
```sh
python -m venv env
```

Sử dụng môi trường:
```sh
source env/bin/activate
```

Cài đặt các gói phụ thuộc:
```sh
pip install -r require.txt
```

## Sử dụng
Sử dụng môi trường:
```sh
source env/bin/activate
```

Gộp file:
```sh
python __main__.py đường/dẫn/1.pdf đường/dẫn/2.pdf
```

Hoặc
```sh
python __main__.py đường/dẫn/1.pdf đường/dẫn/2.pdf -o xuất/file.pdf
```