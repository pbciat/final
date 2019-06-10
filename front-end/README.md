[![Build Status](https://travis-ci.org/pbciat/pbc-final.svg?branch=master)](https://travis-ci.org/pbciat/pbc-final)

# IAT 網頁版

## Dependencies

需使用 `Python 3.5+`，並且安裝 [`websockets`](https://websockets.readthedocs.io/) 套件:

```bash
pip install websockets
```

## 執行

### Mac or Linux

1. 下載 [server.zip](https://pbciat.github.io/server.zip)

2. 在 Terminal 執行下方指令：

    ```bash
    python3 path/to/server.zip
    ```

3. 前往 https://pbciat.github.io



#### 步驟 2. Alternative:

```bash
curl https://pbciat.github.io/server.zip > temp.zip
python3 temp.zip || rm temp.zip
```

### Windows

1. 下載 [server.zip](https://pbciat.github.io/server.zip)

2. 在命令提示字元執行 `server.py`：
    
    ```bash
    python C:\<path>\server.zip
    ```

3. 前往 https://pbciat.github.io

