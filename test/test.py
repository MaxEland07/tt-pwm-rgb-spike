# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # Full brightness on all three channels: every colour output stays high.
    dut.ui_in.value = 0b00111111
    await ClockCycles(dut.clk, 6)
    assert int(dut.uo_out.value) & 0b111 == 0b111

    # Everything off: no colour output goes high.
    dut.ui_in.value = 0
    await ClockCycles(dut.clk, 6)
    assert int(dut.uo_out.value) & 0b111 == 0
