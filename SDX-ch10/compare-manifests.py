def name_with_diff_hash(manifest1, manifest2):
    diff = {}
    for name in manifest1.keys():
        if manifest1[name] != manifest2[name]:
            if name in diff:
                diff[name] += [manifest1[name], manifest2[name]]
            else:
                diff[name] = [manifest1[name], manifest2[name]]
    return diff