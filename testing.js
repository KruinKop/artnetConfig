let string = `<node><sys><ip>0A14187C</ip><mask>FFFFFF00</mask><mac>0023C40011F7</mac><name>smurfs-node-15</name></sys><artnet><inp0>000A 0200</inp0><inp1>000A 0200</inp1><inp2>0002 0200</inp2><inp3>0008 01FF</inp3><inp4>0011 01F8</inp4><inp5>0005 0200</inp5><inp6>0001 0200</inp6><inp7>0009 0200</inp7><inp8>0008 0200</inp8><inp9>0009 0200</inp9></artnet><fieldbus><out0>00 0000 0000</out0><out1>00 0000 0000</out1><out2>02 0001 0200</out2><out3>02 0601 00C8</out3><out4>02 044F 0176</out4><out5>02 0001 01FF</out5></fieldbus></node>`

let error = "";
for (let i = 430; i < 440; i++) {
    error += string[i];
    if (i === 436) {
        console.log(string[i]);
    }
}
console.log(error)