#!/bin/bash
set -e

PATTERNS=(
  "global\['!\'\]="
  "global\[\"!\"\]="
  "\\\\u0000"
  "\\.split\\(''\\.split\\(''\\.split"
  "fromCharCode.*for.*in"
  "eval\\(.*atob"
  "exec\\(.*Buffer"
  "Function\\(.*String"
  "require.*\\['require'\\]"
  "module.*\\['module'\\]"
  "__dirname.*__filename"
  "child_process.*execSync"
  "https.*request.*POST"
  "crypto.*createCipher"
  "btoa\\|atob"
  "setTimeout.*0.*code"
  "\\[\\d+\\]\\.split.*shuffle"
)

SUSPICIOUS_FILES=$(find . -type f \( -name "*.js" -o -name "*.mjs" -o -name "*.cjs" -o -name "*.ts" -o -name "*.tsx" -o -name "*.jsx" -o -name "*.json" -o -name "*.sh" -o -name "*.env" \) \
  ! -path "*/node_modules/*" ! -path "*/.git/*" ! -path "*/dist/*" ! -path "*/build/*" ! -path "*/.next/*" ! -path "*/coverage/*" ! -path "*/vendor/*" 2>/dev/null || true)

MALWARE_FOUND=0
REPORT_FILE="malicious-scan-report.txt"

> "$REPORT_FILE"

for FILE in $SUSPICIOUS_FILES; do
  for PATTERN in "${PATTERNS[@]}"; do
    if grep -E "$PATTERN" "$FILE" 2>/dev/null | grep -qv "test\|spec"; then
      echo "🚨 MALWARE DETECTED in $FILE" >> "$REPORT_FILE"
      echo "Pattern: $PATTERN" >> "$REPORT_FILE"
      echo "---" >> "$REPORT_FILE"
      MALWARE_FOUND=1
    fi
  done
done

if [[ $MALWARE_FOUND -eq 1 ]]; then
  echo "Malware scan report saved to $REPORT_FILE"
  exit 1
fi

echo "✅ SCAN PASSED - No malware detected" | tee -a "$REPORT_FILE"
exit 0
