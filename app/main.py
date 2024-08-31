import json
import sys
import bencodepy
import hashlib

# import requests - available if you need it!
# Examples:
#
# - decode_bencode(b"5:hello") -> b"hello"
# - decode_bencode(b"10:hello12345") -> b"hello12345"

bc = bencodepy.Bencode(
    encoding="utf-8",
    encoding_fallback='value',
    dict_ordered=True,
    dict_ordered_sort=True )


def decode_bencode(bencoded_value):


    return bc.decode(bencoded_value)

    if chr(bencoded_value[0]).isdigit():
    
        first_colon_index = bencoded_value.find(b":")
        
        if first_colon_index == -1:
            raise ValueError("Invalid encoded value")
        
        return bencoded_value[first_colon_index+1:]
    
    elif chr(bencoded_value[0]) == 'i':
        return int(bencoded_value[1: -1])

    else:
    
        raise NotImplementedError("Only strings are supported at the moment")

def main():
    command = sys.argv[1]


    if command == "decode":
        bencoded_value = sys.argv[2].encode()

        # json.dumps() can't handle bytes, but bencoded "strings" need to be
        # bytestrings since they might contain non utf-8 characters.
        #
        # Let's convert them to strings for printing to the console.
        def bytes_to_str(data):
            if isinstance(data, bytes):
                return data.decode()

            raise TypeError(f"Type not serializable: {type(data)}")

        print(json.dumps(decode_bencode(bencoded_value), default=bytes_to_str))

    elif command == "info":
        with open(sys.argv[2], "rb") as f:
            data = f.read()
            parsed = decode_bencode(data)
            info_hash = hashlib.sha1(bencodepy.encode(parsed["info"])).hexdigest()
            print("Tracker URL:", parsed["announce"])
            print("Length:", parsed["info"]["length"])
            print(f"Info Hash: {info_hash}")
            print("Piece Length:", parsed["info"]["piece length"])
            print("Piece Hashes: ", )

            for i in range(0, len(parsed["info"]["pieces"]), 20):
                print(parsed["info"]["pieces"][i : i + 20].hex())



    else:
        raise NotImplementedError(f"Unknown command {command}")


if __name__ == "__main__":
    main()
