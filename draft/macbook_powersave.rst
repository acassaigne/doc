https://zignar.net/2012/12/20/linux-on-a-macbook-air/
sudo pm-powersave true

http://askubuntu.com/questions/285434/is-there-a-power-saving-application-similar-to-jupiter/285681#285681
http://linrunner.de/en/tlp/docs/tlp-linux-advanced-power-management.html

 etc / modprobe.d

 etc  modprobe.d    $ more i915.conf
options i915 i915_enable_rc6=1
options i915 i915_enable_fbc=1
options i915 lvds_downclock=1
 etc  modprobe.d    $ 
