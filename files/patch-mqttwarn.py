--- mqttwarn.py.orig	2018-03-26 15:16:18.829280000 +0000
+++ mqttwarn.py	2018-03-26 15:20:22.456537000 +0000
@@ -83,6 +83,8 @@
         self.cleansession = False
         self.protocol     = 3
 
+        self.libdir       = ''
+
         self.logformat    = '%(asctime)-15s %(levelname)-5s [%(module)s] %(message)s'
         self.logfile      = LOGFILE
         self.loglevel     = 'DEBUG'
@@ -999,7 +1001,7 @@
         modulefile = 'services/%s.py' % module
 
         try:
-            service_plugins[service]['module'] = load_module(modulefile)
+            service_plugins[service]['module'] = load_module(cf.libdir + '/' + modulefile)
             logging.debug("Service %s loaded" % (service))
         except Exception, e:
             logging.error("Can't load %s service (%s): %s" % (service, modulefile, str(e)))
