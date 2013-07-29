/*jslint browser: true */
/*global _: false, angular: false */

// Configuration constants. Overrides can be specified under window.settings

(function () {
  'use strict';

  var SETTINGS = {
    apiBaseUrl: '/',
    staticBaseUrl: '/static/',
    baseUrl: '/'
  };

  angular.module('client.config', []).

  config(['$provide', function ($provide) {
    var overrides = window.settings || {};
    $provide.constant('settings', _.extend(SETTINGS, overrides));
  }]);

})();
