/**
 * This is a script to download moodle assets.
 * It's copied into the chrome/firefox/safari/ie (and by god, please don't use something below ie9) devtools.
 **/

(function() {
    'use strict';
    /* globals jQuery, clear, copy */

    var COOKIE = document.cookie;
    var DOWNLOAD_CMD = "wget '%LINK%' --content-disposition --adjust-extension --header 'Cookie: %COOKIE%'".replace('%COOKIE%', COOKIE);

    var WHITE_LIST = 'pdf Exercise Teil Präsentation Tutor Uebung Zusatz Übung Lösung Vorlesung Aufzeichnung Multiplizierer Klausur Tutorial History supplementary video pdfs interfaces'.toLowerCase().split(' '),
        BLACK_LIST = 'Forum Gruppe Sprechstunden'.toLowerCase().split(' ');

    init();

    function init() {
        if (typeof jQuery === 'undefined') {
            loadScript('https://code.jquery.com/jquery.js', getLinks);
        } else {
            getLinks();
        }
    }

    function filter(index, item) {
        var txt = jQuery(item).text().toLowerCase();

        function reduceFn(isListed, current) {
            return isListed || ~txt.indexOf(current);
        }

        var blacklisted = BLACK_LIST.reduce(reduceFn, false);
        var whitelisted = WHITE_LIST.reduce(reduceFn, false);

        if (!whitelisted || blacklisted) console.error("BLACKLISTED:", txt);
        else console.log("WHITELISTED:", txt);

        return whitelisted && !blacklisted;
    }

    function getLinks() {
        clear();
        var links = jQuery('body .instancename')
            .filter(filter)
            .closest('a')
            .map(function(index, item) {
                var downloadLink = jQuery(item).attr('href');
                console.info("DOWLOADING", downloadLink);
                return DOWNLOAD_CMD.replace('%LINK%', downloadLink);
            })
            .toArray();

        try {
            copy(links.join(';'));
            console.log('Copied to your clipboard');
        } catch (e) {
            console.error('Your dev tools doesn\'t have the copy function');
        }
    }

    function loadScript(url, callback) {
        var script = document.createElement("script");
        script.type = "text/javascript";
        script.onload = callback;
        script.src = url;
        document.getElementsByTagName("head")[0].appendChild(script);
    }
})();
