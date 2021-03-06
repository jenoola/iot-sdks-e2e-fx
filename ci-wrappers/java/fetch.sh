# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

cd /sdk
[ $? -eq 0 ] || { echo "cd shared failed"; exit 1; }

export temp=$1

if [ -s /${temp}/source.tar.gz ]; then 
  mkdir /${temp}/source && 
  tar -zxf /${temp}/source.tar.gz -C /${temp}/source 
  rsync --recursive --checksum --update /${temp}/source/ . 
else
  git fetch origin && git reset --hard origin/$HORTON_BASE_BRANCH
  git checkout $HORTON_SHA
fi

