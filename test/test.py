# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, Timer


@cocotb.test()
async def test_project(dut):

    dut._log.info("Start")

    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0

    dut.rst_n.value = 0

    await Timer(25, unit="us")

    dut.rst_n.value = 1

    # Sync to a clean clock edge before sampling starts,
    # to avoid a race between reset release and the clock edge
    await FallingEdge(dut.clk)
    await Timer(100, unit="ns")

    expected = 0

    for i in range(16):

        await FallingEdge(dut.clk)
        await Timer(100, unit="ns")

        expected = (expected + 1) & 0xF

        actual = int(dut.uo_out.value) & 0xF

        dut._log.info(
            f"Expected = {expected:04b}, Actual = {actual:04b}"
        )

        assert actual == expected, (
            f"Counter error: Expected {expected:04b}, "
            f"got {actual:04b}"
        )

    dut._log.info("Counter reached 1111")

    await FallingEdge(dut.clk)
    await Timer(100, unit="ns")

    actual = int(dut.uo_out.value) & 0xF

    assert actual == 0, (
        f"Counter did not wrap to 0000, got {actual:04b}"
    )

    dut._log.info("4-bit ripple counter test passed")
