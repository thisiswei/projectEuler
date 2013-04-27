ps1 = function() {
  var result = 0
  for (var i = 0; i < 1000; i++) {
    if (i % 3 == 0 || i % 5 == 0) {
      result += i;
    }
  }
  return result;
}

ps2 = function(n) {
  var i,
      a = 1,
      b = 2,
      sum = 2;

  for (i = 3; i < n; i = a + b) {
    if (i % 2 === 0) sum += i;
    a = b;
    b = i;
  }
  return sum; 
};

isPrime = function(n) {
  var factor = 0;
  for (var i = 2; i < n; i++) {
    if (n % i == 0) factor += 1;
    if (factor > 0) return false;
  }
  return true;
};

isPrime2 = function(n) {
  if (n % 2 == 0) return (n === 2);
  var m = Math.sqrt(n);
  for (var i = 3; i <= m; i+=2) {
    if (n % i == 0) return false;
  }
  return true;
};
    
ps3 = function(){
  var n = 600851475143;
  var ans = 1;
  while (n % 2 === 0) {
    n /= 2;
    ans = 2;
  }
  while (n % 3 === 0) {
    n /= 3;
    ans = 3;
  }
  for (p = 5, q = 7; n != 1; p += 6, q += 6) {
    while (n % p === 0) {
      n /= p;
      ans = p;
    }
    while (n % q === 0) {
      n /= q;
      ans = q;
    }
  }
  return ans
}

ps3 = function(){
  var n = 600851475143;
  var ans = 1;
  while (n % 2 === 0) {
    n /= 2;
    ans = 2;
  }
  while (n % 3 === 0) {
    n /= 3;
    ans = 3;
  }
  for (p = 5, q = 7; n != 1; p += 6, q += 6) {
    while (n % p === 0) {
      n /= p;
      ans = p;
    }
    while (n % q === 0) {
      n /= q;
      ans = q;
    }
  }
  return ans
}

isPal = function(n) {
  n = n.toString();
  return n === n.split('').reverse().join('')
}

//why this not generate right reuslt????fuck!!
ps4 = function() {
  var max = 999 * 999,
      min = 100 * 100;
  for (var i = max; i > min; i--) {
    if (!isPal(i)) continue;
    for (var j = 999; j > 100; j--) {
      if (i % j === 0) {
        if ((i/j).toString().length === 3) return [i, j];
      }
    }
  }
}

ps4_2 = function () {
  var ans = 0;
  for ( x = 999; x >= 100; x--) {
    for (y = x; y >= 100; y--) {
      n = x * y;
      if (n > ans) {
        s = String(n);
        if (s.slice(0, 1) !== s.slice(-1)) continue;
        if (s.slice(1, 2) !== s.slice(-2, -1)) continue;
        if (s.slice(2, 3) !== s.slice(-3, -2)) continue;
        ans = n;
      }
    }
  }
  return ans
}

ps5 = function() { 
  var range = [],
      i,
      j = 2520;
  for (i = 1; i<21; i++) {
    range.push(i);
  }
  var divisible = function(n) {
    return range.reduce(function(a, b) {return n % (a*b) === 0;});
  }
  while (true) {
    if (divisible(j)) return j;
    j += 2520;
  }
}

ps6 = function(){
  var i,
      j,
      ans1 = 0,
      acc = 0;
  for (i = 1; i < 101; i++) {
    ans1 += Math.pow(i, 2);
    acc  += i ;
  }
  return Math.pow(acc, 2) - ans1;
}

ps7 = function(n){
  var cnt = 2,
      start = 3;
  for (start; cnt < n; start+=2) {
    if (isPrime2(start)) cnt += 1;
  }
  return start;
};

ps9 = function() {
  var i,
      j,
      k;
  var trigle = function(a, b, c) {
    return a*a + b*b === c*c;
  };
  for (i; i < 1000; i++) {
    for (j = i + 1; i + j + j < 1000; j++) {
      k = 1000 - i - j;
      if (i*i + j*j == k*k) break;
    }
  }
};

