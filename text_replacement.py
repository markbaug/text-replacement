def text_replacement(marker,replacement,line):
	marker_start=line.find(marker)
	marker_end=marker_start+len(marker)
	replaced=line[:marker_start]+replacement+line[marker_end:]
	return replaced