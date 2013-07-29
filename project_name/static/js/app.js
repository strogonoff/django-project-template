/*jslint browser: true */
/*global sprintf: false */

(function () {
  'use strict';

  window.angular.module('client', [
    'client.config',
    'client.utility',
    'client.controllers']).

  config([
    '$locationProvider',
    '$httpProvider',
    function ($locationProvider, $httpProvider) {
      $httpProvider.defaults.headers.
        post['Content-Type'] = 'application/x-www-form-urlencoded';
      $httpProvider.defaults.headers.
        common['X-Requested-With'] = 'XMLHttpRequest';

      $locationProvider.html5Mode(false);

      window.Messenger.options = {
        extraClasses: 'messenger-fixed messenger-on-top messenger-on-right',
        theme: 'future'};
    }
  ]).

  factory('$exceptionHandler', [
    '$log',
    function ($log) {
      return function (exception, cause) {
        // Log to console
        $log.error.apply($log, arguments);

        // Show to user
        var msg = sprintf("Error: %s", exception.message);
        if (cause) { msg = sprintf("%s. %s", msg, cause); }
        window.Messenger().post({
          type: 'error',
          hideAfter: 0,
          showCloseButton: true,
          message: msg
        });
      };
    }
  ]).

  run([
    '$rootScope',
    'settings',
    function ($rootScope, settings) {
      // To make settings accessible from HTML
      $rootScope.settings = settings;
    }
  ]);

})();
