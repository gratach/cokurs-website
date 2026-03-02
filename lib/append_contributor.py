def append_contributor(old_contributors, new_contributor, newProjectAuthorIndexMappedToCombinedAuthorIndex):
    old_contributors_modified = [{k:v for k,v in p.items() if k in {"vorname", "nachname"}} for p in old_contributors]
    new_contributor_modified = {k:v for k,v in new_contributor.items() if k in {"vorname", "nachname"}}
    if new_contributor_modified in old_contributors_modified:
        array_position = old_contributors_modified.index(new_contributor_modified)
        newProjectAuthorIndexMappedToCombinedAuthorIndex[new_contributor["id"]] = old_contributors[array_position]["id"]
        # Update contributor
        if "upload-ok" in new_contributor:
            old_contributors[array_position]["upload-ok"] = new_contributor["upload-ok"]
        if "verlauf" in new_contributor:
            verlauf = old_contributors[array_position].setdefault("verlauf")
            for v in new_contributor["verlauf"]:
                if not v in verlauf:
                    verlauf.append(v)
    else:
        new_contributor_modified = new_contributor.copy()
        new_contributor_modified["id"] = len(old_contributors)
        newProjectAuthorIndexMappedToCombinedAuthorIndex[new_contributor["id"]] = len(old_contributors)
        old_contributors.append(new_contributor_modified)