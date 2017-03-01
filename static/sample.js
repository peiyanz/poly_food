! function(e) {
    if ("object" == typeof exports && "undefined" != typeof module) module.exports = e();
    else if ("function" == typeof define && define.amd) define([], e);
    else {
        var t;
        t = "undefined" != typeof window ? window : "undefined" != typeof global ? global : "undefined" != typeof self ? self : this, t.MapboxDraw = e()
    }
}(function() {
    return function e(t, n, r) {
        function o(s, a) {
            if (!n[s]) {
                if (!t[s]) {
                    var u = "function" == typeof require && require;
                    if (!a && u) return u(s, !0);
                    if (i) return i(s, !0);
                    var c = new Error("Cannot find module '" + s + "'");
                    throw c.code = "MODULE_NOT_FOUND", c
                }
                var l = n[s] = {
                    exports: {}
                };
                t[s][0].call(l.exports, function(e) {
                    var n = t[s][1][e];
                    return o(n ? n : e)
                }, l, l.exports, e, t, n, r)
            }
            return n[s].exports
        }
        for (var i = "function" == typeof require && require, s = 0; s < r.length; s++) o(r[s]);
        return o
    }({
        1: [function(e, t, n) {
            "use strict";
            var r = e("./src/setup"),
                o = e("./src/options"),
                i = e("./src/api"),
                s = e("./src/constants"),
                a = function(e, t) {
                    e = o(e);
                    var n = {
                        options: e
                    };
                    t = i(n, t), n.api = t;
                    var a = r(n);
                    return t.onAdd = a.onAdd, t.onRemove = a.onRemove, t.types = s.types, t.options = e, t
                };
            t.exports = function(e) {
                a(e, this)
            }
        }, {
            "./src/api": 23,
            "./src/constants": 24,
            "./src/options": 58,
            "./src/setup": 60
        }],
        2: [function(e, t, n) {}, {}],
        3: [function(e, t, n) {
            (function(e) {
                function t(e, t) {
                    for (var n = 0, r = e.length - 1; r >= 0; r--) {
                        var o = e[r];
                        "." === o ? e.splice(r, 1) : ".." === o ? (e.splice(r, 1), n++) : n && (e.splice(r, 1), n--)
                    }
                    if (t)
                        for (; n--; n) e.unshift("..");
                    return e
                }

                function r(e, t) {
                    if (e.filter) return e.filter(t);
                    for (var n = [], r = 0; r < e.length; r++) t(e[r], r, e) && n.push(e[r]);
                    return n
                }
                var o = /^(\/?|)([\s\S]*?)((?:\.{1,2}|[^\/]+?|)(\.[^.\/]*|))(?:[\/]*)$/,
                    i = function(e) {
                        return o.exec(e).slice(1)
                    };
                n.resolve = function() {
                    for (var n = "", o = !1, i = arguments.length - 1; i >= -1 && !o; i--) {
                        var s = i >= 0 ? arguments[i] : e.cwd();
                        if ("string" != typeof s) throw new TypeError("Arguments to path.resolve must be strings");
                        s && (n = s + "/" + n, o = "/" === s.charAt(0))
                    }
                    return n = t(r(n.split("/"), function(e) {
                        return !!e
                    }), !o).join("/"), (o ? "/" : "") + n || "."
                }, n.normalize = function(e) {
                    var o = n.isAbsolute(e),
                        i = "/" === s(e, -1);
                    return e = t(r(e.split("/"), function(e) {
                        return !!e
                    }), !o).join("/"), e || o || (e = "."), e && i && (e += "/"), (o ? "/" : "") + e
                }, n.isAbsolute = function(e) {
                    return "/" === e.charAt(0)
                }, n.join = function() {
                    var e = Array.prototype.slice.call(arguments, 0);
                    return n.normalize(r(e, function(e, t) {
                        if ("string" != typeof e) throw new TypeError("Arguments to path.join must be strings");
                        return e
                    }).join("/"))
                }, n.relative = function(e, t) {
                    function r(e) {
                        for (var t = 0; t < e.length && "" === e[t]; t++);
                        for (var n = e.length - 1; n >= 0 && "" === e[n]; n--);
                        return t > n ? [] : e.slice(t, n - t + 1)
                    }
                    e = n.resolve(e).substr(1), t = n.resolve(t).substr(1);
                    for (var o = r(e.split("/")), i = r(t.split("/")), s = Math.min(o.length, i.length), a = s, u = 0; u < s; u++)
                        if (o[u] !== i[u]) {
                            a = u;
                            break
                        }
                    for (var c = [], u = a; u < o.length; u++) c.push("..");
                    return c = c.concat(i.slice(a)), c.join("/")
                }, n.sep = "/", n.delimiter = ":", n.dirname = function(e) {
                    var t = i(e),
                        n = t[0],
                        r = t[1];
                    return n || r ? (r && (r = r.substr(0, r.length - 1)), n + r) : "."
                }, n.basename = function(e, t) {
                    var n = i(e)[2];
                    return t && n.substr(-1 * t.length) === t && (n = n.substr(0, n.length - t.length)), n
                }, n.extname = function(e) {
                    return i(e)[3]
                };
                var s = "b" === "ab".substr(-1) ? function(e, t, n) {
                    return e.substr(t, n)
                } : function(e, t, n) {
                    return t < 0 && (t = e.length + t), e.substr(t, n)
                }
            }).call(this, e("_process"))
        }, {
            _process: 4
        }],
        4: [function(e, t, n) {
            function r() {
                throw new Error("setTimeout has not been defined")
            }

            function o() {
                throw new Error("clearTimeout has not been defined")
            }

            function i(e) {
                if (p === setTimeout) return setTimeout(e, 0);
                if ((p === r || !p) && setTimeout) return p = setTimeout, setTimeout(e, 0);
                try {
                    return p(e, 0)
                } catch (t) {
                    try {
                        return p.call(null, e, 0)
                    } catch (t) {
                        return p.call(this, e, 0)
                    }
                }
            }

            function s(e) {
                if (f === clearTimeout) return clearTimeout(e);
                if ((f === o || !f) && clearTimeout) return f = clearTimeout, clearTimeout(e);
                try {
                    return f(e)
                } catch (t) {
                    try {
                        return f.call(null, e)
                    } catch (t) {
                        return f.call(this, e)
                    }
                }
            }

            function a() {
                g && h && (g = !1, h.length ? y = h.concat(y) : m = -1, y.length && u())
            }

            function u() {
                if (!g) {
                    var e = i(a);
                    g = !0;
                    for (var t = y.length; t;) {
                        for (h = y, y = []; ++m < t;) h && h[m].run();
                        m = -1, t = y.length
                    }
                    h = null, g = !1, s(e)
                }
            }

            function c(e, t) {
                this.fun = e, this.array = t
            }

            function l() {}
            var p, f, d = t.exports = {};
            ! function() {
                try {
                    p = "function" == typeof setTimeout ? setTimeout : r
                } catch (e) {
                    p = r
                }
                try {
                    f = "function" == typeof clearTimeout ? clearTimeout : o
                } catch (e) {
                    f = o
                }
            }();
            var h, y = [],
                g = !1,
                m = -1;
            d.nextTick = function(e) {
                var t = new Array(arguments.length - 1);
                if (arguments.length > 1)
                    for (var n = 1; n < arguments.length; n++) t[n - 1] = arguments[n];
                y.push(new c(e, t)), 1 !== y.length || g || i(u)
            }, c.prototype.run = function() {
                this.fun.apply(null, this.array)
            }, d.title = "browser", d.browser = !0, d.env = {}, d.argv = [], d.version = "", d.versions = {}, d.on = l, d.addListener = l, d.once = l, d.off = l, d.removeListener = l, d.removeAllListeners = l, d.emit = l, d.binding = function(e) {
                throw new Error("process.binding is not supported")
            }, d.cwd = function() {
                return "/"
            }, d.chdir = function(e) {
                throw new Error("process.chdir is not supported")
            }, d.umask = function() {
                return 0
            }
        }, {}],
        5: [function(e, t, n) {
            function r(e) {
                var t, n = 0;
                switch (e.type) {
                    case "Polygon":
                        return o(e.coordinates);
                    case "MultiPolygon":
                        for (t = 0; t < e.coordinates.length; t++) n += o(e.coordinates[t]);
                        return n;
                    case "Point":
                    case "MultiPoint":
                    case "LineString":
                    case "MultiLineString":
                        return 0;
                    case "GeometryCollection":
                        for (t = 0; t < e.geometries.length; t++) n += r(e.geometries[t]);
                        return n
                }
            }

            function o(e) {
                var t = 0;
                if (e && e.length > 0) {
                    t += Math.abs(s(e[0]));
                    for (var n = 1; n < e.length; n++) t -= Math.abs(s(e[n]))
                }
                return t
            }

            function s(e) {
                var t, n, r, o, s, c, l = 0,
                    p = e.length;
                if (p > 2) {
                    for (i = 0; i < p; i++) i === p - 2 ? (o = p - 2, s = p - 1, c = 0) : i === p - 1 ? (o = p - 1, s = 0, c = 1) : (o = i, s = i + 1, c = i + 2), t = e[o], n = e[s], r = e[c], l += (a(r[0]) - a(t[0])) * Math.sin(a(n[1]));
                    l = l * u.RADIUS * u.RADIUS / 2
                }
                return l
            }

            function a(e) {
                return e * Math.PI / 180
            }
            var u = e("wgs84");
            t.exports.geometry = r, t.exports.ring = s
        }, {
            wgs84: 6
        }],
        6: [function(e, t, n) {
            t.exports.RADIUS = 6378137, t.exports.FLATTENING = 1 / 298.257223563, t.exports.POLAR_RADIUS = 6356752.3142
        }, {}],
        7: [function(e, t, n) {
            function r(e) {
                for (var t = s(), n = o(e), r = 0; r < n.length; r++) t.include(n[r]);
                return t
            }
            var o = e("geojson-coords"),
                i = e("traverse"),
                s = e("extent");
            t.exports = function(e) {
                return r(e).bbox()
            }, t.exports.polygon = function(e) {
                return r(e).polygon()
            }, t.exports.bboxify = function(e) {
                return i(e).map(function(e) {
                    e && "string" == typeof e.type && (e.bbox = r(e).bbox(), this.update(e))
                })
            }
        }, {
            extent: 8,
            "geojson-coords": 10,
            traverse: 13
        }],
        8: [function(e, t, n) {
            function r() {
                return this instanceof r ? (this._bbox = [1 / 0, 1 / 0, -(1 / 0), -(1 / 0)], void(this._valid = !1)) : new r
            }
            t.exports = r, r.prototype.include = function(e) {
                return this._valid = !0, this._bbox[0] = Math.min(this._bbox[0], e[0]), this._bbox[1] = Math.min(this._bbox[1], e[1]), this._bbox[2] = Math.max(this._bbox[2], e[0]), this._bbox[3] = Math.max(this._bbox[3], e[1]), this
            }, r.prototype.union = function(e) {
                return this._valid = !0, this._bbox[0] = Math.min(this._bbox[0], e[0]), this._bbox[1] = Math.min(this._bbox[1], e[1]), this._bbox[2] = Math.max(this._bbox[2], e[2]), this._bbox[3] = Math.max(this._bbox[3], e[3]), this
            }, r.prototype.bbox = function() {
                return this._valid ? this._bbox : null
            }, r.prototype.contains = function(e) {
                return this._valid ? this._bbox[0] <= e[0] && this._bbox[1] <= e[1] && this._bbox[2] >= e[0] && this._bbox[3] >= e[1] : null
            }, r.prototype.polygon = function() {
                return this._valid ? {
                    type: "Polygon",
                    coordinates: [
                        [
                            [this._bbox[0], this._bbox[1]],
                            [this._bbox[2], this._bbox[1]],
                            [this._bbox[2], this._bbox[3]],
                            [this._bbox[0], this._bbox[3]],
                            [this._bbox[0], this._bbox[1]]
                        ]
                    ]
                } : null
            }
        }, {}],
        9: [function(e, t, n) {
            t.exports = function(e, t) {
                function n(e) {
                    return Array.isArray(e) && e.length && "number" == typeof e[0] ? [e] : e.reduce(function(e, t) {
                        return Array.isArray(t) && Array.isArray(t[0]) ? e.concat(n(t)) : (e.push(t), e)
                    }, [])
                }
                return n(e)
            }
        }, {}],
        10: [function(e, t, n) {
            var r = e("geojson-normalize"),
                o = e("geojson-flatten"),
                i = e("./flatten");
            t.exports = function(e) {
                if (!e) return [];
                var t = o(r(e)),
                    n = [];
                return t.features.forEach(function(e) {
                    e.geometry && (n = n.concat(i(e.geometry.coordinates)))
                }), n
            }
        }, {
            "./flatten": 9,
            "geojson-flatten": 11,
            "geojson-normalize": 12
        }],
        11: [function(e, t, n) {
            function r(e, t) {
                switch (e && e.type || null) {
                    case "FeatureCollection":
                        return e.features = e.features.reduce(function(e, t) {
                            return e.concat(r(t))
                        }, []), e;
                    case "Feature":
                        return r(e.geometry).map(function(t) {
                            return {
                                type: "Feature",
                                properties: JSON.parse(JSON.stringify(e.properties)),
                                geometry: t
                            }
                        });
                    case "MultiPoint":
                        return e.coordinates.map(function(e) {
                            return {
                                type: "Point",
                                coordinates: e
                            }
                        });
                    case "MultiPolygon":
                        return e.coordinates.map(function(e) {
                            return {
                                type: "Polygon",
                                coordinates: e
                            }
                        });
                    case "MultiLineString":
                        return e.coordinates.map(function(e) {
                            return {
                                type: "LineString",
                                coordinates: e
                            }
                        });
                    case "GeometryCollection":
                        return e.geometries;
                    case "Point":
                    case "Polygon":
                    case "LineString":
                        return [e];
                    default:
                        return e
                }
            }
            t.exports = r
        }, {}],
        12: [function(e, t, n) {
            function r(e) {
                if (!e || !e.type) return null;
                var t = o[e.type];
                return t ? "geometry" === t ? {
                    type: "FeatureCollection",
                    features: [{
                        type: "Feature",
                        properties: {},
                        geometry: e
                    }]
                } : "feature" === t ? {
                    type: "FeatureCollection",
                    features: [e]
                } : "featurecollection" === t ? e : void 0 : null
            }
            t.exports = r;
            var o = {
                Point: "geometry",
                MultiPoint: "geometry",
                LineString: "geometry",
                MultiLineString: "geometry",
                Polygon: "geometry",
                MultiPolygon: "geometry",
                GeometryCollection: "geometry",
                Feature: "feature",
                FeatureCollection: "featurecollection"
            }
        }, {}],
        13: [function(e, t, n) {
            function r(e) {
                this.value = e
            }

            function o(e, t, n) {
                var r = [],
                    o = [],
                    s = !0;
                return function e(a) {
                    function u() {
                        if ("object" == typeof f.node && null !== f.node) {
                            f.keys && f.node_ === f.node || (f.keys = h(f.node)), f.isLeaf = 0 == f.keys.length;
                            for (var e = 0; e < o.length; e++)
                                if (o[e].node_ === a) {
                                    f.circular = o[e];
                                    break
                                }
                        } else f.isLeaf = !0, f.keys = null;
                        f.notLeaf = !f.isLeaf, f.notRoot = !f.isRoot
                    }
                    var c = n ? i(a) : a,
                        l = {},
                        p = !0,
                        f = {
                            node: c,
                            node_: a,
                            path: [].concat(r),
                            parent: o[o.length - 1],
                            parents: o,
                            key: r.slice(-1)[0],
                            isRoot: 0 === r.length,
                            level: r.length,
                            circular: null,
                            update: function(e, t) {
                                f.isRoot || (f.parent.node[f.key] = e), f.node = e, t && (p = !1)
                            },
                            delete: function(e) {
                                delete f.parent.node[f.key], e && (p = !1)
                            },
                            remove: function(e) {
                                y(f.parent.node) ? f.parent.node.splice(f.key, 1) : delete f.parent.node[f.key], e && (p = !1)
                            },
                            keys: null,
                            before: function(e) {
                                l.before = e
                            },
                            after: function(e) {
                                l.after = e
                            },
                            pre: function(e) {
                                l.pre = e
                            },
                            post: function(e) {
                                l.post = e
                            },
                            stop: function() {
                                s = !1
                            },
                            block: function() {
                                p = !1
                            }
                        };
                    if (!s) return f;
                    u();
                    var d = t.call(f, f.node);
                    return void 0 !== d && f.update && f.update(d), l.before && l.before.call(f, f.node), p ? ("object" != typeof f.node || null === f.node || f.circular || (o.push(f), u(), g(f.keys, function(t, o) {
                        r.push(t), l.pre && l.pre.call(f, f.node[t], t);
                        var i = e(f.node[t]);
                        n && m.call(f.node, t) && (f.node[t] = i.node), i.isLast = o == f.keys.length - 1, i.isFirst = 0 == o, l.post && l.post.call(f, i), r.pop()
                    }), o.pop()), l.after && l.after.call(f, f.node), f) : f
                }(e).node
            }

            function i(e) {
                if ("object" == typeof e && null !== e) {
                    var t;
                    if (y(e)) t = [];
                    else if (a(e)) t = new Date(e.getTime ? e.getTime() : e);
                    else if (u(e)) t = new RegExp(e);
                    else if (c(e)) t = {
                        message: e.message
                    };
                    else if (l(e)) t = new Boolean(e);
                    else if (p(e)) t = new Number(e);
                    else if (f(e)) t = new String(e);
                    else if (Object.create && Object.getPrototypeOf) t = Object.create(Object.getPrototypeOf(e));
                    else if (e.constructor === Object) t = {};
                    else {
                        var n = e.constructor && e.constructor.prototype || e.__proto__ || {},
                            r = function() {};
                        r.prototype = n, t = new r
                    }
                    return g(h(e), function(n) {
                        t[n] = e[n]
                    }), t
                }
                return e
            }

            function s(e) {
                return Object.prototype.toString.call(e)
            }

            function a(e) {
                return "[object Date]" === s(e)
            }

            function u(e) {
                return "[object RegExp]" === s(e)
            }

            function c(e) {
                return "[object Error]" === s(e)
            }

            function l(e) {
                return "[object Boolean]" === s(e)
            }

            function p(e) {
                return "[object Number]" === s(e)
            }

            function f(e) {
                return "[object String]" === s(e)
            }