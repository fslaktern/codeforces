const std = @import("std");
const expect = @import("std").testing.expect;

pub fn main() !void {
    var x: i16 = 0;

    const stdin = std.io.getStdIn().reader();
    const stdout = std.io.getStdOut().writer();

    var buf: [4]u8 = undefined;
    var n: u8 = 0;

    const n_str = try stdin.readUntilDelimiterOrEof(&buf, '\n');
    if (n_str) |bytes| {
        n = try std.fmt.parseInt(u8, bytes, 10);
        if (n > 150) return error.InputTooLarge;
    } else {
        try stdout.print("Failed to read n\n", .{});
        return;
    }

    while (n > 0) {
        var op_buf: [4]u8 = undefined;
        const op_str = try stdin.readUntilDelimiterOrEof(&op_buf, '\n');
        if (op_str) |op_bytes| {
            if (op_bytes.len < 3) {
                try stdout.print("Invalid operaiton input\n", .{});
                return;
            }
            const op = op_bytes[1];
            if (op == '+') {
                x += 1;
            } else {
                x -= 1;
            }
        } else {
            try stdout.print("Failed to read operation\n", .{});
            return;
        }
        n -= 1;
    }

    try stdout.print("{d}\n", .{x});
}
