public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
    ArrayList<ArrayList<Integer>> finalList = new ArrayList<ArrayList<Integer>>();
    if(root == null)
        return finalList;

    ArrayList<Integer> list = new ArrayList<Integer>();
    list.add(root.val);
    subSolution(root, sum-root.val, finalList, list);
    return finalList;
}


public void subSolution(TreeNode tree, int sum, ArrayList<ArrayList<Integer>> finalList, ArrayList<Integer> list){
    if(tree.left==null && tree.right==null && sum==0){
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        tempList.addAll(list);
        finalList.add(tempList);
    }

    if(tree.left != null){
        list.add(tree.left.val);
        subSolution(tree.left, sum-tree.left.val, finalList, list);
        list.remove(list.size()-1);
    }

    if(tree.right!=null){
        list.add(tree.right.val);
        subSolution(tree.right, sum-tree.right.val, finalList, list);
        list.remove(list.size()-1);
    }
}
