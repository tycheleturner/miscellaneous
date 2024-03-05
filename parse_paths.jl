#!/usr/bin/env julia

#set the argument parser package
using ArgParse

#define the arguments
function get_parsed_args()
    set = ArgParseSettings()
    @add_arg_table set begin
        "-i", "--input"
        help = "input file name"
        required = true
        arg_type = String
    end
    return parse_args(set)
end

#get the last part of a path, if not input file than output help message
try
    args = get_parsed_args()
    filename = args["input"]
    open(filename) do f
        for line in eachline(f)
            println(join([split(line, "/")[end]], '\t'))
        end
    end
catch e
    println("Error: $(e.message)")
    println("Usage: julia script.jl -i <input_file>")
    exit(1)
end

