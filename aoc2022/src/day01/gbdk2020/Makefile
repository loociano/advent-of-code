AS = lcc -c
CC = lcc -Wa-l -Wl-m

BIN = aoc2022day01.gb
OBJS = aoc2022day01.o

all: $(BIN)

%.s: %.ms
	maccer -o $@ $<

$(BIN): $(OBJS)
	$(CC) -o $(BIN) $(OBJS)

clean:
	rm -rf $(BIN) $(OBJS) *~

