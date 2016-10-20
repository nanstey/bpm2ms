# bpm2ms

Given a value in Beats Per Minute, returns a list of rhythmic divisions in Milliseconds.

This is especially useful for audio production to find ultra fast compression/gate/delay values that are in time with the music.

# Usage

Run the file using Python. Pass it a value in BPM.

```
python bpm2ms.py 120
```
returns:
```
  Whole = 2000.00ms
  Half = 1000.00ms
  Quarter = 500.00ms
  Eighth = 250.00ms
  16th = 125.00ms
  32th = 62.50ms
  64th = 31.25ms
  128th = 15.62ms
  256th = 7.81ms
  512th = 3.91ms
  1024th = 1.95ms

  Dotted Half = 1500.00ms
  Dotted Quarter = 750.00ms
  Dotted Eighth = 375.00ms
  Dotted 16th = 187.50ms
  Dotted 32th = 93.75ms
  Dotted 64th = 46.88ms
  Dotted 128th = 23.44ms
  Dotted 256th = 11.72ms
  Dotted 512th = 5.86ms
  Dotted 1024th = 2.93ms

  Triplet Half = 666.67ms
  Triplet Quarter = 333.33ms
  Triplet Eighth = 166.67ms
  Triplet 16th = 83.33ms
  Triplet 32th = 41.67ms
  Triplet 64th = 20.83ms
  Triplet 128th = 10.42ms
  Triplet 256th = 5.21ms
  Triplet 512th = 2.60ms
  Triplet 1024th = 1.30ms
```
optional arguments:
```
  -h, --help      show this help message and exit
  -a, --all       print all values DEFAULT
  -s, --straight  print straight values
  -d, --dotted    print dotted values
  -t, --triplet   print triplet values
```
# Credits

Written by Noel Anstey
