#!/usr/bin/tcsh


#####################################
#
# selektieren von
#  - season
#  - hemisphaere
#  - Jahresgang abziehen
#
######################################


set year_start = 1979
set year_last = 2014

set mon='djfm'
set hemisphaere = .S

set pfadin = '/modelnob1/global/NOAA_20CR/daily/'
set pfadout = '/model2/jriebold/model3/paleo/NOAA_20CR/daymean_'${year_start}'-'${year_last}'/'


if ( $mon == 'djf' ) set smon="01,02,12"
if ( $mon == 'djfm' ) set smon="01,02,03,12"
if ( $mon == 'ndjf' ) set smon="01,02,11,12"

#if ( ${hemisphaere} == ".N" ) set box="0,360,0,90"
if ( ${hemisphaere} == ".N" ) set box="-90,90,30,88"
if ( ${hemisphaere} == ".S" ) set box="0,360,-88,-20"

cd $pfadout

set year=$year_start
while ( $year <= $year_last ) 

cdo -sellonlatbox,${box} -selmon,${smon} -selname,prmsl ${pfadin}/prmsl.${year}.nc slp.${year}.nc

@ year = $year + 1
end

cdo cat slp.????.nc dummy.nc
rm slp.????.nc


cdo divc,100 dummy.nc slp${hemisphaere}_${mon}.nc
rm dummy.nc

#Jahresgang berechnen & abzeihen
cdo sub slp${hemisphaere}_${mon}.nc -ydaymean slp${hemisphaere}_${mon}.nc slp${hemisphaere}_${mon}_aac.nc

#set filein=slp${hemisphaere}_${mon}
#cdo divc,100 ${filein}.nc dummy.nc
#mv dummy.nc ${filein}.nc 
#cdo ydaymean ${filein}.nc ${filein}_ydaymean.nc
#cdo sub ${filein}.nc  ${filein}_ydaymean.nc ${filein}_aac.nc



