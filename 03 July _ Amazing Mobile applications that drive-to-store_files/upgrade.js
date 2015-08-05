/* Test old browsers */
(function(){
	// Test at least SVG support
	// and getElementsByClassName support
	// https://github.com/Modernizr/Modernizr/blob/master/feature-detects/svg/asimg.js
	var skipped = document.cookie.replace(/(?:(?:^|.*;\s*)upgrade_skip\s*\=\s*([^;]*).*$)|^.*$/, "$1") === "true";
	if(!skipped && !(document.implementation.hasFeature('http://www.w3.org/TR/SVG11/feature#Image', '1.1') && typeof document.getElementsByClassName == "function")){
		// a visible node (here a text node) is required by IE to handle <style> and <script> tags
		//language=HTML
		var html = "IEFIX" + "<style>html, body{\n\t\toverflow: hidden;\n\t\tpadding: 0;\n\t\tmargin: 0;\n\t}\n\t.upgrade{\n\t\tposition: fixed;\n\t\theight: 100%;\n\t\twidth: 100%;\n\t\tz-index: 9999999;\n\t\tfont-family: \"Asap\", sans-serif;\n\t\tbackground: #e0d1a5 url(\"$base/images/pattern6_repeat.png\");\n\t\toverflow: auto;\n\t}\n\t.upgrade_content{\n\t\tposition: absolute;\n\t\theight: 100%;\n\t\twidth: 100%;\n\t\tbackground: url(\"$base/images/flint-computer.png\") center 60% no-repeat;\n\t}\n\t.upgrade_title{\n\t\tposition: absolute;\n\t\toverflow: hidden;\n\t\tclip: rect(0px, 0px, 0px, 0px);\n\t\twidth: 1px;\n\t\theight: 1px;\n\t}\n\t.upgrade_line1{\n\t\tdisplay: block;\n\t\ttext-indent: 99999px;\n\t\toverflow: hidden;\n\t\twhite-space: nowrap;\n\t\tfont-size: 34px;\n\t\twidth: 320px;\n\t\tmargin: 0 -160px;\n\t\theight: 250px;\n\t\tposition: absolute;\n\t\tleft: 50%;\n\t\ttop: 3%;\n\t\tbackground: url(\"$base/images/old-browser_en.png\") no-repeat;\n\t}\n\t.upgrade_line2{\n\t\tposition: absolute;\n\t\tbottom: 12%;\n\t\twidth: 100%;\n\t\ttext-align: center;\n\t\tletter-spacing: 0.1em;\n\t\tdisplay: block;\n\t\tbackground: white;\n\t\ttext-transform: uppercase;\n\t\tcolor: #5ca1be;\n\t\tfont-size: 20px;\n\t\tpadding: 22px 0;\n\t\twhite-space: nowrap;\n\t\tfont-weight: bold;\n\t\tline-height: 24px;\n\t}\n\t.upgrade_link{\n\t\tcolor: #f87335;\n\t\ttext-decoration: none;\n\t\tborder-bottom: 5px solid #f87335;\n\t\tpadding-bottom: 17px;\n\t}\n\t.upgrade_skip{\n\t\tposition: absolute;\n\t\tbottom: 6%;\n\t\tleft: 50%;\n\t\tdisplay: block;\n\t\ttext-indent: 99999px;\n\t\toverflow: hidden;\n\t\twhite-space: nowrap;\n\t\twidth: 53px;\n\t\theight: 51px;\n\t\tmargin: -25.5px -26.5px;\n\t\tbackground: url(\"$base/images/logo4.png\") no-repeat;\n\t}\n</style>\n<div id=\"upgrade\" class=\"upgrade\" role=\"dialog\" aria-labelledby=\"upgrade-title\">\n\t<div class=\"upgrade_content\">\n\t\t<h1 id=\"upgrade_title\" class=\"upgrade_title\">This website is not optimized for your browser</h1>\n\t\t<p>\n\t\t\t<span class=\"upgrade_line1\">Your browser was created for human caves</span><br>\n\t\t\t<span class=\"upgrade_line2\">Please <a class=\"upgrade_link\" href=\"http://browsehappy.com/\">upgrade it</a> and be a normal being.</span>\n\t\t</p>\n\t\t<p><a id=\"upgrade_skip\" class=\"upgrade_skip\" href=\"\" title=\"I can\'t (cookies must be enabled)\">03July</a></p>\n\t</div>\n</div>";
		html = html.replace(/\$base/gi, document.documentElement.getAttribute("data-theme-base"));
		var body = document.body;
		body.insertAdjacentHTML("afterbegin", html);
		// Remove IEFIX text node
		body.removeChild(body.firstChild);
		document.getElementById("upgrade_skip").onclick = function(){
			document.cookie = "upgrade_skip=true; expires=Fri, 31 Dec 9999 23:59:59 GMT; path=/";
		};
		var upgradeElement = document.getElementById("upgrade");
		// Capture the focus in upgradeElement
		function onfocus(event){
			var target = event ? event.target : window.event.srcElement/*IE fallback*/;
			if (!upgradeElement.contains(target)) {
				upgradeElement.focus();
			}
		}
		document.onfocus = onfocus;
		// IE specific
		document.onfocusin = onfocus;
		// Will ignore all further script errors
		window.onerror = function(){};
	}
})();