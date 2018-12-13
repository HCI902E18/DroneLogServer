var mymap = L.map('mapid', {
    zoomSnap: 0.25
}).setView([57.01313018035709, 9.991430319089478], 13);

L.tileLayer('https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
    maxZoom: 20,
}).addTo(mymap);


$(document).ready(function () {
    var features = L.featureGroup();
    features.addTo(mymap);

    $(document).on('click', 'a.folder', function () {
        $.get('/log/' + $(this).data('folder'), function (points) {
            features.clearLayers();
            let is_emergency = false;

            for (var i = 0; i < points.length - 1; i++) {
                let point = points[i];
                let next_point = points[i + 1];

                let from = [point['lat'], point['lon']];
                let to = [next_point['lat'], next_point['lon']];

                if (point['flyingState'] === 'emergency') {
                    if (!is_emergency)
                        features.addLayer(
                            L.marker([point['lat'], point['lon']])
                        );
                    is_emergency = true;
                } else {
                    is_emergency = false;
                }

                let polyline = L.polyline(
                    [from, to]
                );

                features.addLayer(polyline);
            }

            if (features.getLayers().length !== 0)
                mymap.fitBounds(features.getBounds());
        });
    });

    $(document).on('click', 'a.delete', function () {
        $(this).parent().remove();
    });
});