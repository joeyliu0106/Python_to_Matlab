clc
clear

% i=0;
t = tcpclient('192.168.6.3', 22);
while(1)
    if t.NumBytesAvailable > 0
        output = read(t);
        data = char(output(1:3));
        pwrcmd = str2double(data)
    end
end
clear t;