(function() {

const num = "93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000".split("");

  for (let i =0;i < num.length; i++) {
    num[i] = parseInt(num[i]);
  }


  let sum = num.reduce(function (a, b) {
    return a +b;
  });


  console.log(sum);
})();
