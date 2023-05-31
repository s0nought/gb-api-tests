#!/bin/bash

_script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pushd "${_script_dir}" > /dev/null

pytest -v -m "smoke"

read

popd > /dev/null
