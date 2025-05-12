ymaps.ready(init);
function init() {
    var myMap = new ymaps.Map('map', {
        center: [50, 50],
        zoom: 9
    });

    var vacancyElement = document.getElementById('map');
    var address = vacancyElement.getAttribute('data-address');
    console.log('Адрес для геокодирования:', address);

    ymaps.geocode(address, {
        results: 1
    }).then(function (res) {
        var firstGeoObject = res.geoObjects.get(0),
            coords = firstGeoObject.geometry.getCoordinates(),
            bounds = firstGeoObject.properties.get('boundedBy');

        firstGeoObject.options.set('preset', 'islands#darkBlueDotIconWithCaption');
        firstGeoObject.properties.set('iconCaption', address);

        myMap.geoObjects.add(firstGeoObject);
        myMap.setBounds(bounds, {
            checkZoomRange: true
        });

        // запись в консоль для справки
        console.log('Все данные геообъекта: ', firstGeoObject.properties.getAll());
        console.log('Метаданные ответа геокодера: ', res.metaData);
        console.log('Метаданные геокодера: ', firstGeoObject.properties.get('metaDataProperty.GeocoderMetaData'));
        console.log('precision', firstGeoObject.properties.get('metaDataProperty.GeocoderMetaData.precision'));
        console.log('Тип геообъекта: %s', firstGeoObject.properties.get('metaDataProperty.GeocoderMetaData.kind'));
        console.log('Название объекта: %s', firstGeoObject.properties.get('name'));
        console.log('Описание объекта: %s', firstGeoObject.properties.get('description'));
        console.log('Полное описание объекта: %s', firstGeoObject.properties.get('text'));
        console.log('\nГосударство: %s', firstGeoObject.getCountry());
        console.log('Населенный пункт: %s', firstGeoObject.getLocalities().join(', '));
        console.log('Адрес объекта: %s', firstGeoObject.getAddressLine());
        console.log('Наименование здания: %s', firstGeoObject.getPremise() || '-');
        console.log('Номер здания: %s', firstGeoObject.getPremiseNumber() || '-');
    });
}
