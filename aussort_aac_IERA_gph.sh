#!/usr/bin/tcsh


#####################################
#
# selektieren von
#  - season
#  - hemisphaere
#  - Jahresgang abziehen
#
######################################
set echo on

set year_start = 1979
set year_last = 2016
set level=700
set mon='all'
set hemisphaere = .S

set pfadin = '/glomod/nobackup/global/IERA/'
set pfadout = '/glomod/user/jriebold/IERA/daymean_'${year_start}'-'${year_last}'/'


if ( $mon == 'djf' ) set smon="01,02,12"
if ( $mon == 'djfm' ) set smon="01,02,03,12"
if ( $mon == 'ndjf' ) set smon="01,02,11,12"
if ( $mon == 'all' ) set smon=('01' '02' '03' '04' '05' '06' '07' '08' '09' '10' '11' '12')

#if ( ${hemisphaere} == ".N" ) set box="0,360,0,90"
if ( ${hemisphaere} == ".N" ) set box="-90,90,30,88"
if ( ${hemisphaere} == ".S" ) set box="0,360,-88,-20"

cd $pfadout

set year=$year_start
while ( $year <= $year_last ) 
	foreach month($smon)
		cdo -sellonlatbox,${box} -selmon,${month} -selname,zprs -sellevel,$level ${pfadin}gph.daymean.${year}${month}.nc gph_${level}.${year}${month}.nc
	end

@ year = $year + 1

end

cdo cat gph_${level}.??????.nc gph_${level}_${hemisphaere}_${mon}.nc
rm gph_${level}.??????.nc



#Jahresgang berechnen & abzeihen
cdo sub  gph_${level}_${hemisphaere}_${mon}.nc -ydaymean  gph_${level}_${hemisphaere}_${mon}.nc dummy2.nc
rm dummy.nc
ncwa -a levels dummy2.nc  gph_${level}_${hemisphaere}_${mon}_aac.nc
rm dummy2.nc
#set filein=slp${hemisphaere}_${mon}
#cdo divc,100 ${filein}.nc dummy.nc
#mv dummy.nc ${filein}.nc 
#cdo ydaymean ${filein}.nc ${filein}_ydaymean.nc
#cdo sub ${filein}.nc  ${filein}_ydaymean.nc ${filein}_aac.nc



