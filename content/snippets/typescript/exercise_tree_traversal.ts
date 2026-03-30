class Node {
  val: number;
  left: Node | null;
  right: Node | null;
  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function inorder(root: Node | null, res: number[]): void {
  if (!root) return;
  inorder(root.left, res);
  res.push(root.val);
  inorder(root.right, res);
}

const root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);

const res: number[] = [];
inorder(root, res);
console.log(res);
type TreeNode = { value: number; left?: TreeNode; right?: TreeNode };

function inorder(root?: TreeNode): number[] {
  if (!root) return [];
  return [...inorder(root.left), root.value, ...inorder(root.right)];
}

const tree: TreeNode = { value: 2, left: { value: 1 }, right: { value: 3 } };
console.log(inorder(tree));
