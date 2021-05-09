var points;
var pointsMore;
var polygon;
var map;


function initializeMap() {

    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 11,
        center: new google.maps.LatLng(42.347727, -83.058014),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    });

    var polygon = createPolygons(pointsMore);
    //this is where the problem is...check nesting.
    polygon.setMap(map);

}


function createPolygons(pointsMore) {
    for (var y = 0; y < data.features.length; y++) {
        var points = data.features[y];
        for (var z = 0; points.geometry.length; z++) {
            var pointsMore = points.geometry[z];



    var coords = pointsMore.coordinates;
    var paths = [];
    $.each(coords,function(i,n){
        $.each(n, function(j,o){
           var path = [];
           $.each(o,function(k,p){
               var ll = new google.maps.LatLng(p[1],[0]);
               path.push(ll);
           });
           paths.push(path); 
        });
    });
    var polygon = new google.maps.Polygon({
        paths: paths,
        strokeColor: "#FF7800",
        strokeOpacity: 1,
        strokeWeight: 2,
        fillColor: "#46461F",
        fillOpacity: 0.25
    });
    return polygon; 
        }   
    }
}