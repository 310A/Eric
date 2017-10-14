/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
  let right = left = up = down = 0;
  for(const i in moves) {
    if(moves[i]  === 'R')right++;
    else if(moves[i] === 'L')left++;
    else if(moves[i] === 'U')up++;
    else down++;
  }
  return (right === left && up === down);
};