from datetime import datetime


def tail(f, n):
    assert n >= 0
    pos, lines = n+1, []
    while len(lines) <= n:
        try:
            f.seek(-pos, 2)
        except IOError:
            f.seek(0)
            break
        finally:
            lines = list(f)
        pos *= 2
    return lines[-n:]


f1 = open('file1.txt', 'r+')
f2 = open('file2.txt', 'r')
t = open('res.txt', 'r+')
# removes closing lines from sub1
store = f1.readlines()
t.writelines(store[:-4])
t.writelines("\n")

# starting index for sub2
start = int(tail(t, 4)[0])
start_time_str = (tail(t, 4)[1])
start_time = datetime.strptime(start_time_str[17:25], '%H:%M:%S')
time_zero = datetime.strptime('00:00:00', '%H:%M:%S')
#print((start_time - time_zero + time_obj).time())


store2 = f2.readlines()
g = [-1]
for i in range(len(store2)):
    if store2[i] == "\n":
        g.append(i)

for i in range(len(g)):
    start += 1
    t.writelines(str(start)+"\n")

    try:
        s1 = datetime.strptime(store2[g[i]+2:g[i+1]][0][:8], '%H:%M:%S')
        s2 = datetime.strptime(store2[g[i]+2:g[i+1]][0][17:25], '%H:%M:%S')
        t.writelines(str((start_time - time_zero + s1).time()) + store2[g[i]+2:g[i+1]][0][8:17] + str(
            (start_time - time_zero + s2).time()) + store2[g[i]+2:g[i+1]][0][25:])
        t.writelines(store2[g[i]+3:g[i+1]])
        t.writelines("\n")
    except:
        t.writelines(store2[g[i]+2:])
f1.close()
f2.close()
t.close()
