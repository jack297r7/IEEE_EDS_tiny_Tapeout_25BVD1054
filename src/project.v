/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_jack (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);

    reg [3:0] count;

    always @(negedge clk or negedge rst_n) begin
        if (!rst_n)
            count[0] <= 1'b0;
        else
            count[0] <= ~count[0];
    end

    always @(negedge count[0] or negedge rst_n) begin
        if (!rst_n)
            count[1] <= 1'b0;
        else
            count[1] <= ~count[1];
    end

    always @(negedge count[1] or negedge rst_n) begin
        if (!rst_n)
            count[2] <= 1'b0;
        else
            count[2] <= ~count[2];
    end

    always @(negedge count[2] or negedge rst_n) begin
        if (!rst_n)
            count[3] <= 1'b0;
        else
            count[3] <= ~count[3];
    end

    assign uo_out[3:0] = count;
    assign uo_out[7:4] = 4'b0000;

    assign uio_out = 8'b00000000;
    assign uio_oe  = 8'b00000000;

    wire _unused = &{ena, ui_in, uio_in, 1'b0};

endmodule
