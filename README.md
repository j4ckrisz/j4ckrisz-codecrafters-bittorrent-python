# j4ckrisz-codecrafters-bittorrent-python

## Usage

Download
```
python3 app/main.py download_piece -o /tmp/test-piece-0 sample.torrent 0
```

info
```
python3 app/main.py info sample.torrent
```

peers
```
python3 app/main.py peers sample.torrent
```

handshake
```
python3 app/main.py handshake sample.torrent <peer_ip>:<peer_port>
```
