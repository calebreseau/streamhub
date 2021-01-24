initplayer($('#sources').val().split(',')[0]);
$('#sources').on('change', function() {
    initplayer($('#sources').val().split(',')[0]);
});

function initplayer(pmagnet){
    $('#download').attr('href',$('#sources').val().split(',')[0]);
    $('#player').html('');
    window.webtor = window.webtor || [];
        window.webtor.push({
            id: 'player',
            magnet: pmagnet,
            on: function(e) {
                if (e.name == window.webtor.TORRENT_FETCHED) {
                    console.log('Torrent fetched!', e.data);
                }
                if (e.name == window.webtor.TORRENT_ERROR) {
                    console.log('Torrent error!');
                }
            },
            poster: 'https://via.placeholder.com/150/0000FF/808080?Text=Sintel',
            subtitles: [
                {
                    srclang: 'en',
                    label: 'test',
                    src: 'https://raw.githubusercontent.com/andreyvit/subtitle-tools/master/sample.srt',
                }
            ],
            lang: 'en',
            i18n: {
                en: {
                    common: {
                        "prepare to play": "Preparing Video Stream... Please Wait...",
                    },
                    stat: {
                        "seeding": "Seeding",
                        "waiting": "Client initialization",
                        "waiting for peers": "Waiting for peers",
                        "from": "from",
                    },
                },
            },
        });
}