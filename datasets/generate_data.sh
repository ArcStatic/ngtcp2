#playback buffer of 3 frames, 10% loss, 100 frames to send in total, 2000 RTP timestamp increment, quiet mode, send 60 frames per second, partial reliability
../examples/server -b 3 -t 0.1 -l 100 -i 2000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_10L_100F_2000D_60R_server.txt &

../client -b 3 -e -a 2000 -q 127.0.0.1 5004 > PARTIAL_3B_10L_100F_2000D_60R_client.txt &

sleep 1m


../examples/server -b 3 -t 0.05 -l 100 -i 2000 -q -f 60 127.0.0.1 5004 ../test-ca/rsa/ca.key test-ca/rsa/ca.cert > PARTIAL_3B_5L_100F_2000D_60R_server.txt &

../client -b 3 -e -a 2000 -q 127.0.0.1 5004 > PARTIAL_3B_5L_100F_2000D_60R_client.txt &

sleep 1m

