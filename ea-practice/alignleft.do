* Align text in string variables to the left
ds, has(type string)

foreach v in `r(varlist)' { 
	local type : type `v' 
	local type : subinstr local type "str" "" 
	format `v' %-`type's
}
