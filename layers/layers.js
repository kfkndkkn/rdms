ol.proj.proj4.register(proj4);
//ol.proj.get("EPSG:4326").setExtent([98.565278, -10.198917, 140.703833, 3.500250]);
var wms_layers = [];


        var lyr_GoogleHybrid_0 = new ol.layer.Tile({
            'title': 'Google Hybrid',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: '&nbsp;&middot; <a href="https://www.google.at/permissions/geoguidelines/attr-guide.html">Map data ©2015 Google</a>',
                url: 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}'
            })
        });
var format_LokasiStasiun_1 = new ol.format.GeoJSON();
var features_LokasiStasiun_1 = format_LokasiStasiun_1.readFeatures(json_LokasiStasiun_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_LokasiStasiun_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_LokasiStasiun_1.addFeatures(features_LokasiStasiun_1);
var lyr_LokasiStasiun_1 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_LokasiStasiun_1, 
                style: style_LokasiStasiun_1,
                popuplayertitle: 'Lokasi Stasiun',
                interactive: false,
                title: 'Lokasi Stasiun'
            });
var format_Overview_2 = new ol.format.GeoJSON();
var features_Overview_2 = format_Overview_2.readFeatures(json_Overview_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:4326'});
var jsonSource_Overview_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Overview_2.addFeatures(features_Overview_2);
var lyr_Overview_2 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_Overview_2, 
                style: style_Overview_2,
                popuplayertitle: 'Overview',
                interactive: true,
    title: 'Overview<br />\
    <img src="styles/legend/Overview_2_0.png" /> 0.01 - 0.088<br />\
    <img src="styles/legend/Overview_2_1.png" /> 0.088 - 0.166<br />\
    <img src="styles/legend/Overview_2_2.png" /> 0.166 - 0.244<br />\
    <img src="styles/legend/Overview_2_3.png" /> 0.244 - 0.322<br />\
    <img src="styles/legend/Overview_2_4.png" /> 0.322 - 0.4<br />' });

lyr_GoogleHybrid_0.setVisible(true);lyr_LokasiStasiun_1.setVisible(true);lyr_Overview_2.setVisible(true);
var layersList = [lyr_GoogleHybrid_0,lyr_LokasiStasiun_1,lyr_Overview_2];
lyr_LokasiStasiun_1.set('fieldAliases', {'IDUNIT': 'IDUNIT', 'NAMA UNIT': 'Lokus', 'LONGITUDE': 'LONGITUDE', 'LATITUDE': 'LATITUDE', });
lyr_Overview_2.set('fieldAliases', {'IDUNIT': 'IDUNIT', 'NAMA UNIT': 'Lokus', 'LONGITUDE': 'LONGITUDE', 'LATITUDE': 'LATITUDE', 'Gamma Dose Rate': 'Gamma Dose Rate (uSv/h)', 'LAST UPDATE': 'Last Updated on', });
lyr_LokasiStasiun_1.set('fieldImages', {'IDUNIT': 'TextEdit', 'NAMA UNIT': 'TextEdit', 'LONGITUDE': 'TextEdit', 'LATITUDE': 'TextEdit', });
lyr_Overview_2.set('fieldImages', {'IDUNIT': 'TextEdit', 'NAMA UNIT': 'TextEdit', 'LONGITUDE': 'TextEdit', 'LATITUDE': 'TextEdit', 'Gamma Dose Rate': 'TextEdit', 'LAST UPDATE': 'TextEdit', });
lyr_LokasiStasiun_1.set('fieldLabels', {'IDUNIT': 'hidden field', 'NAMA UNIT': 'inline label - visible with data', 'LONGITUDE': 'hidden field', 'LATITUDE': 'hidden field', });
lyr_Overview_2.set('fieldLabels', {'IDUNIT': 'hidden field', 'NAMA UNIT': 'inline label - visible with data', 'LONGITUDE': 'hidden field', 'LATITUDE': 'hidden field', 'Gamma Dose Rate': 'inline label - visible with data', 'LAST UPDATE': 'inline label - always visible', });
lyr_Overview_2.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});