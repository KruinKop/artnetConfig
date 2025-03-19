import socket
import multiprocessing as mp
from time import sleep
# from colour import Color
artnetip = "10.20.24.124"
#artnetip = "127.0.0.1"
#artnetip = "192.168.15.20"
artnetport = 6454

patchlst = [300]#,1,2,3,4,5,6,7,8,9]

def write_artnet(qa,sync,patchlist):
    sock_out = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    artsend = []                #big array of arrays with universes data
    for i in patchlist:         #patchlist is array of universes to send to
        empty = []
        for j in range(512):    #512 channels to drive
            empty.append(0)     #build a whole universe of data
        artsend.append(empty)   #make an array of an array of universes
    sequence = 0
    while True:                 #go into infinity loop for sending data
        sync.get()
        sequence = (sequence+1) % 256
        while not qa.empty():   #check if queue is empty or not. if not empty: patch new data in buffer.
            art_raw = qa.get()  #get new data from queue
            artsend[art_raw[0]] = art_raw[1]    #data is array of array: first is universe, second is data
        head = b'Art-Net\x00\x00\x50\x00\x0e' + sequence.to_bytes(1,'little') + b'\x00'
        for i in range(len(patchlist)): #send all universes defined in patchlist
            data = head+patchlist[i].to_bytes(2,'little') # add universe number
            data += len(artsend[i]).to_bytes(2,'big')   #length of universe
            for d in artsend[i]:
                data += d.to_bytes(1,'big')             #convert data to bytes
            sock_out.sendto(data,(artnetip,artnetport)) #and last send out the data
        artsync = b'Art-Net\x00\00\x52\x00\x0e\x00\x00'
        sock_out.sendto(artsync,(artnetip,artnetport)) #and last send out the data

if __name__ == "__main__":
    aro_qa = mp.SimpleQueue()
    aro_sync = mp.SimpleQueue()
    aro = mp.Process(target=write_artnet, args=(aro_qa,aro_sync,patchlst))
    aro.start()     #start dmx stream
    while True:
        sleep(0.05)
        for lp_j in range(len(patchlst)):
            tosend = [lp_j,[]]
            for i in range(0,512,4):
                tosend[1].extend([int(255),int(0),int(0),int(0)])
            aro_qa.put(tosend)
        for i in range(5):
            sleep(0.01)
            aro_sync.put('1')
    quit()