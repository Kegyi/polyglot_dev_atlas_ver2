import os
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(ROOT, 'content', 'pages', 'course', 'exercises.json')

with open(PAGE, 'r', encoding='utf-8') as f:
    data = json.load(f)

changes = []

def process_block_list(blocks, group_diff=None):
    for b in blocks:
        # b is a block dict with id, title, content
        bid = b.get('id','')
        # check if block id signals difficulty
        if 'beginner' in bid:
            diff = 'beginner'
        elif 'intermediate' in bid:
            diff = 'intermediate'
        elif 'advanced' in bid:
            diff = 'advanced'
        else:
            diff = group_diff
        # walk content
        for item in b.get('content', []):
            walk_item(item, diff, parent_id=bid)

def walk_item(item, diff, parent_id=''):
    if not isinstance(item, dict):
        return
    itype = item.get('type')
    if itype == 'code':
        if 'path' in item:
            return
        name = item.get('name')
        if not name:
            return
        new_path = f"exercises/{diff}/{name}" if diff else f"exercises/{name}"
        item.pop('name', None)
        item['path'] = new_path
        changes.append({'name': name, 'path': new_path, 'parent': parent_id})
    # nested blocks
    if itype == 'blocks' and 'blocks' in item:
        process_block_list(item['blocks'], group_diff=diff)
    # generic nested content
    if 'content' in item and isinstance(item['content'], list):
        for it in item['content']:
            walk_item(it, diff, parent_id)

# Top-level: find blocks under content and process
for top in data.get('content', []):
    if isinstance(top, dict) and 'blocks' in top:
        # top may contain many blocks; process each
        for sub in top['blocks']:
            # determine group difficulty from parent's id if present
            parent_id = sub.get('id','')
            if 'beginner' in parent_id:
                group = 'beginner'
            elif 'intermediate' in parent_id:
                group = 'intermediate'
            elif 'advanced' in parent_id:
                group = 'advanced'
            else:
                group = None
            process_block_list([sub], group)

# Write back
if changes:
    with open(PAGE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

print('Applied group-based path changes:', len(changes))
for c in changes:
    print(f"- {c['name']} -> {c['path']} (parent: {c['parent']})")
print('Done')
