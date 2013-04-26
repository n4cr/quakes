function IranGeo() {
  var height=300,
      width=300;

  function my(selection) {
    iran(selection);
  }
  
  function iran(selection) {
    selection.each(function(data, i) {
      // plot iran here
      var projection = d3.geo.albers();
      var path = d3.geo.path().projection(projection);
 
      var element = d3.select(this);
      var svg = element.selectAll('svg').data([data]);
      //Enter
      var svgEnter = svg.enter()
          .append('svg')
          .append('g')
          .attr('class', 'graph')
          .attr('transform', 'translate(' + width / 2 + ',' + height / 2 + ')'); 

      svg.attr('width', width)
         .attr('height', height);

    });

  }
  my.width = function(_) {
    if(!arguments.length) return width;
    width = _;
    return my;
  }

  my.height = function(_) {
    if(!arguments.length) return height;
    height = _;
    return my;
  }
  return my;
  var irantop = 
}
