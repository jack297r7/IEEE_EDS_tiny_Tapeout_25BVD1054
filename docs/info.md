## How it works

This project implements a 4-bit ripple counter. Each flip-flop stage
toggles on the falling edge of the previous stage's output, starting
from the main clock. This produces a binary count from 0000 to 1111
that wraps back to 0000, with each bit rippling through the chain
with a small propagation delay characteristic of ripple counters.

## How to test

Reset the design by pulling `rst_n` low then high. On each falling
edge of `clk`, the 4-bit count on `uo_out[3:0]` increments by 1,
wrapping from 1111 back to 0000. The testbench (`test.py`) verifies
this behavior over 16 clock cycles.
