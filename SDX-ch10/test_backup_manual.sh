BACKUPS=/tmp/backups
rm -rf $BACKUPS
python backup_oop.py sample_dir $BACKUPS
tree --charset ascii $BACKUPS
