#!/bin/sh

analytics_script=$(cat <<'EOF'
 <script>
    const script = document.createElement('script');
    script.src = 'https://metrics.cyb.ai/js/script.js';
    script.setAttribute('data-domain', location.host);
    script.defer = true;
    document.body.appendChild(script);
  </script>
EOF
)


find $GITHUB_WORKSPACE/build -name 'index.html' -exec sh -c '
for file do
  sed "/<\/html>/i $analytics_script" "$file"
done
' sh {} +


