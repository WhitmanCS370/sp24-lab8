BACKUPS=/tmp/backups
rm -rf $BACKUPS
python3 backup.py sample_dir $BACKUPS
tree --charset ascii $BACKUPS
