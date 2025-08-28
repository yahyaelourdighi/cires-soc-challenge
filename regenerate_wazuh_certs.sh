#!/bin/bash

CERT_DIR=~/cires-soc-challenge/configs/wazuh_indexer_ssl_certs

echo "[*] Backing up existing node certificates..."
mkdir -p /tmp/wazuh_node_certs_backup
cp "$CERT_DIR"/wazuh*.pem "$CERT_DIR"/wazuh*.key "$CERT_DIR"/wazuh*.csr /tmp/wazuh_node_certs_backup/ 2>/dev/null

echo "[*] Cleaning old node certificates..."
rm -f "$CERT_DIR"/wazuh*.pem "$CERT_DIR"/wazuh*.key "$CERT_DIR"/wazuh*.csr

echo "[*] Regenerating node certificates..."

# Array of CNs for nodes
declare -A NODES=(
    ["wazuh1-indexer"]="wazuh1-indexer"
    ["wazuh2-indexer"]="wazuh2-indexer"
    ["wazuh3-indexer"]="wazuh3-indexer"
    ["wazuh.master"]="wazuh-master"
    ["wazuh.worker"]="wazuh-worker"
    ["wazuh.dashboard"]="wazuh-dashboard"
)

for node in "${!NODES[@]}"; do
    CN="${NODES[$node]}"
    KEY="$CERT_DIR/$node-key.pem"
    CSR="$CERT_DIR/$node.csr"
    CERT="$CERT_DIR/$node.pem"

    echo "[*] Generating $node certificate..."
    openssl genrsa -out "$KEY" 2048
    openssl req -new -key "$KEY" -subj "/C=US/ST=California/L=California/O=Wazuh/CN=$CN" -out "$CSR"
    openssl x509 -req -in "$CSR" -CA "$CERT_DIR/root-ca.pem" -CAkey "$CERT_DIR/root-ca.key" -CAcreateserial -out "$CERT" -days 365 -sha256
done

echo "[*] Node certificates regenerated successfully!"

