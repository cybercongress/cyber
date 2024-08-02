#!/bin/sh

metas='<meta property="og:title" content="cyber docs">

<meta name="description" content="cyber docs">
<meta property="og:description" content="cyber docs">

<meta property="og:image" content="/static/img/logo.png">'

file="$GITHUB_WORKSPACE/build/index.html"

sed -i "/<\/head>/i\\
$(echo "$metas" | sed 's/$/\\n/' | tr -d '\n')\\
" "$file"
