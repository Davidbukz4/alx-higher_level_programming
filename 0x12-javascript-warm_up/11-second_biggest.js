#!/usr/bin/node
const argList = process.argv.slice(2);

if (!argList[2] || argList.length === 3) {
  console.log('0');
} else {
  let max = parseInt(argList[0]);
  let i;
  let j;
  let maxIndex;
  // get the first max integer
  for (i = 0; i < argList.length; i++) {
    if (max < parseInt(argList[i])) {
      max = argList[i];
      maxIndex = i;
    }
  }
  let secondMax;
  if (maxIndex === 0) {
    secondMax = parseInt(argList[1]);
  } else {
    secondMax = parseInt(argList[0]);
  }
  for (j = 0; j < argList.length; j++) {
    if (j === maxIndex) {
      continue;
    }
    if (secondMax < parseInt(argList[j])) {
      secondMax = parseInt(argList[j]);
    }
  }
  console.log(secondMax);
}
