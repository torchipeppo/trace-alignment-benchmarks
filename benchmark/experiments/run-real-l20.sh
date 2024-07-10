#!/usr/bin/env bash

OUTPUT_DIR=${1:-.}

echo "Output directory: ${OUTPUT_DIR}"

python ./benchmark/experiments/experiment-real.py -l 'l20.xes' -t strips-cpddl --output-dir ${OUTPUT_DIR}/cpddl-REAL-l20 --timeout 3600 --stop-on-timeout
