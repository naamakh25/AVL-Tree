#username - joleentanous
#id1      - 323117416
#name1    - joleen tanous
#id2      - 212385595
#name2    - naama khalil



"""A class represnting a node in an AVL tree"""

class AVLNode(object):
        """Constructor, you are allowed to add more fields. 
        
        @type key: int or None
        @param key: key of your node
        @type value: any
        @param value: data of your node
        """
        def __init__(self, key, value):
                self.key = key
                self.value = value
                self.left = None
                self.right = None #we need to check if the parent of the root should be None or the node None , so it could have a right or left child legally
                self.parent = None #we need to check if the parent of the root should be None or the node None , so it could have a right or left child legally
                self.height = -1
                self.size = 0

        """returns the key

        @rtype: int or None
        @returns: the key of self, None if the node is virtual
        """
        def get_key(self):
                return self.key


        """returns the value

        @rtype: any
        @returns: the value of self, None if the node is virtual
        """
        def get_value(self):
                return self.value


        """returns the left child
        @rtype: AVLNode
        @returns: the left child of self, None if there is no left child (if self is virtual)
        """
        def get_left(self):
                return self.left


        """returns the right child

        @rtype: AVLNode
        @returns: the right child of self, None if there is no right child (if self is virtual)
        """
        def get_right(self):
                return self.right


        """returns the parent 

        @rtype: AVLNode
        @returns: the parent of self, None if there is no parent
        """
        def get_parent(self):
                return self.parent


        """returns the height

        @rtype: int
        @returns: the height of self, -1 if the node is virtual
        """
        def get_height(self):
                return self.height

        """returns the size of the subtree

        @rtype: int
        @returns: the size of the subtree of self, 0 if the node is virtual
        """
        def get_size(self):
                return self.size


        """sets key

        @type key: int or None
        @param key: key
        """
        def set_key(self, key):
                self.key=key
                return None


        """sets value

        @type value: any
        @param value: data
        """
        def set_value(self, value):
                self.value=value
                return None


        """sets left child

        @type node: AVLNode
        @param node: a node
        """
        def set_left(self, node):
                self.left=node
                return None


        """sets right child

        @type node: AVLNode
        @param node: a node
        """
        def set_right(self, node):
                self.right=node
                return None


        """sets parent

        @type node: AVLNode
        @param node: a node
        """
        def set_parent(self, node):
                self.parent=node
                return None


        """sets the height of the node

        @type h: int
        @param h: the height
        """
        def set_height(self, h):
                self.height=h
                



        """sets the size of node

        @type s: int
        @param s: the size
        """
        def set_size(self, s):
                self.size=s
                return None


        """returns whether self is not a virtual node 

        @rtype: bool
        @returns: False if self is a virtual node, True otherwise.
        """
        def is_real_node(self):
                return self.height!=-1

        def get_BF(self): #BF field that helps with the insertion functionality
                return self.left.height-self.right.height

        def Node2Tree(self): #useful for split and join methods, turns a node to a tree with the consideration that the node fulfills an AVL(balanced)binary tree
                Tree=AVLTree()
                Tree.root=self
                L=Tree.root
                if self.parent!=None and self.parent.right.key==self.key:
                        self.parent.right=AVLNode(None,None)
                if self.parent!=None and self.parent.left.key==self.key:
                        self.parent.left=AVLNode(None,None)
                self.parent=None
                while L.left!=None:
                        L=L.left
                Tree.min=L
                return Tree




"""
A class implementing an AVL tree.
"""

class AVLTree(object):

        """
        Constructor, you are allowed to add more fields.  

        """
        def __init__(self):
                self.root = AVLNode(None,None)
                self.min = AVLNode(None,None)
                # add your fields here


        """searches for a node in the dictionary corresponding to the key

        @type key: int
        @param key: a key to be searched
        @rtype: AVLNode
        @returns: node corresponding to key.
        """
        def search(self, key): #we used an iterative solution that uses the binary
                #search advantage, whenever the key is smaller than the current key
                #we move to the left and the same regarding the opposite direction
                s_r=self.root
                while s_r.key!=None:
                        if key==s_r.key:
                                return s_r
                        elif key<s_r.key:
                                s_r=s_r.left
                        else:
                                s_r=s_r.right
                return s_r


        """inserts val at position i in the dictionary

        @type key: int
        @pre: key currently does not appear in the dictionary
        @param key: key of item that is to be inserted to self
        @type val: any
        @param val: the value of the item
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """

        def createRealNode(self,key,val):
                Node=AVLNode(key,val)
                Node.set_height(0)
                Node.set_size(1)
                Node.set_left(AVLNode(None,None)) #stands for Virtual Node
                Node.set_right(AVLNode(None,None))#stands for Virtual Node
                Node.set_parent(None)
                return Node 

        
        def insert(self, key, val):
                Node=self.createRealNode(key,val)
                self.BSTI(Node)
                P=Node.parent
                R_cnt=0
                check=True
                while P!=None:
                        oldH=P.height
                        P.set_height(max(P.left.height,P.right.height)+1)
                        P.set_size(P.left.size+P.right.size+1)
                        bf=P.get_BF()
                        if check==True:
                                if abs(bf) <2 and P.height==oldH: #checks the first condition of the given algorithm in class
                                        check=False
                                elif abs(bf)<2 and P.height!=oldH:
                                        Node=P
                                        P=P.parent
                                
                                else:
                                        if bf==-2:
                                                if P.right.get_BF()==-1:
                                                        self.Left_rotation(Node,P)
                                                        R_cnt=1
                                                        P=Node.parent
                                                
                                                else:
                                                        self.Right_rotation(Node.left,Node)
                                                        self.Left_rotation(Node.parent,Node.parent.parent)
                                                        Node=Node.parent
                                                        P=Node.parent
                                                        R_cnt=2
                                        else:
                                                if P.left.get_BF()==1:
                                                        self.Right_rotation(Node,P)
                                                        R_cnt=1
                                                        P=Node.parent
                                                else:
                                                        self.Left_rotation(Node.right,Node)
                                                        self.Right_rotation(Node.parent,Node.parent.parent)
                                                        Node=Node.parent
                                                        P=Node.parent
                                                        R_cnt=2
                                        check=False
                
                        else:
                                Node=P
                                P=P.parent  
                
                
                return R_cnt

        def Right_rotation(self,A,B):
                G=B.parent
                if G!=None and G.right==B:#checks whether A is a right son or a left son 
                        from_R=True
                else:
                        from_R=False
                B.left=A.right
                B.left.parent=B
                A.right=B
                A.parent=B.parent
                if G!=None and from_R:
                        A.parent.right=A
                elif G!=None:
                        A.parent.left=A
                else:
                        self.root=A
                B.parent=A
                
                B.set_height(max(B.left.height,B.right.height)+1)
                A.set_height(max(A.left.height,A.right.height)+1)
                B.set_size(B.left.size+B.right.size+1)
                A.set_size(A.left.size+A.right.size+1)


        def Left_rotation(self,A,B):
                G=B.parent
                if G!=None and G.left==B:#checks whether A is a right son or a left son 
                        from_L=True
                else:
                        from_L=False
                
                B.right=A.left
                B.right.parent=B
                A.left=B
                A.parent=B.parent
                if G!=None and from_L:
                        A.parent.left=A
                elif G!=None:
                        A.parent.right=A
                else:
                        self.root=A
                B.parent=A
                
                B.set_height(max(B.left.height,B.right.height)+1)
                A.set_height(max(A.left.height,A.right.height)+1)
                B.set_size(B.left.size+B.right.size+1)
                A.set_size(A.left.size+A.right.size+1)
                



        
        def BSTI(self,Node): #binary search tree regular insertion
                y=None
                x=self.root
                while  x.is_real_node()==True:
                        y=x
                        if Node.key<x.key:
                                x=x.left
                        else:
                                x=x.right
                Node.parent=y
                if y==None:
                        self.root=Node
                        self.min=Node
                elif Node.key<y.key:
                        y.left=Node#we could have used set_leftchild
                        if Node.key<self.min.key:
                                self.min=Node
                else:
                        y.right=Node #we could have used set_rightchild
                        if Node.key<self.min.key:
                                self.min=Node





        """deletes node from the dictionary

        @type node: AVLNode
        @pre: node is a real pointer to a node in self
        @rtype: int
        @returns: the number of rebalancing operation due to AVL rebalancing
        """
        
        def delete(self, node):
                node=self.search(node.key)
                check=False
                P=node.parent
                R_cnt=self.BSTD(node)
                while P!=None:
                        oldH=P.height
                        P.set_height(max(P.left.height,P.right.height)+1)
                        P.set_size(P.left.size+P.right.size+1)
                        bf=P.get_BF()
                        if abs(bf)<2 and oldH==P.height:
                                check=True
                        if  check==False:
                                if abs(bf)<2 and oldH!=P.height:
                                        P=P.parent
                                else:
                                        if bf==-2:
                                                if P.right.get_BF()==-1 or P.right.get_BF()==0:
                                                        self.Left_rotation(P.right,P)
                                                        R_cnt+=1
                                                        P=P.parent
                                                else:
                                                        self.Right_rotation(P.right.left,P.right)#(P.left,P)
                                                        self.Left_rotation(P.right,P)#(P.parent,P.parent.parent)
                                                        R_cnt+=2
                                                        P=P.parent
                                                        
                                        else:
                                                if P.left.get_BF()==1 or P.left.get_BF()==0:
                                                        self.Right_rotation(P.left,P)
                                                        R_cnt+=1
                                                        P=P.parent
                                                else:
                                                        self.Left_rotation(P.left.right,P.left)#(P.right,P)
                                                        self.Right_rotation(P.left,P)#(P.parent,P.parent.parent)
                                                        R_cnt+=2
                                                        P=P.parent
                        if P!=None:
                                P=P.parent
                        
                                       
                                
                return R_cnt




        def BSTD(self,Node): #binary search tree regular deletion
                cnt=0
                P=Node.parent
                R=Node.right
                L=Node.left
                self.min=self.successor(Node)
                if P!=None and P.left==Node:#checks whether Node is a right son or a left son 
                        from_L=True
                else:
                        from_L=False
                        
                if L.is_real_node()==False  and R.is_real_node()==False: #the node is a leaf
                        if P==None:#Node is a root #19/5
                                self.root=None
                        elif from_L==True:
                                P.left=AVLNode(None,None)
                        else:
                                P.right=AVLNode(None,None)
                                
                #Node has only one child
                elif  L.is_real_node()==False and R.is_real_node()==True: #has only right child
                        R.parent=P
                        if P==None:#Node is a root #19/5
                                self.root=R
                        elif from_L==True:
                                P.left=R
                        else:
                                P.right=R
                elif L.is_real_node()==True and  R.is_real_node()==False: #has only left child
                        L.parent=P
                        if P==None:#Node is a root #19/5
                                self.root=L
                        elif from_L==True:
                                P.left=L
                        else:
                                P.right=L

                else:#Node two children
                       suc=self.min
                       cnt=self.delete(suc) #deletes suc temporarily 
                       self.replace(suc,Node)

                return cnt
                       
                       
                       
                        
                


                
        def replace(self,new,old):
                new.right=old.right
                new.left=old.left
                new.parent=old.parent
                if old.parent!=None and old.parent.left==old:#checks whether Old is a left son or a left son 
                        from_L=True
                elif old.parent!=None and old.parent.right==old:#checks whether Old is a right son or a left son 
                        from_L=False

                if old.parent!=None:
                        if from_L==True:
                                old.parent.left=new
                        elif from_L==False:
                                old.parent.right=new
                else:
                        self.root=new
                old.left.parent=new
                old.right.parent=new
                old.parent=None #we could have skipped this step
                old.left=None #we could have skipped this step
                old.right=None #we could have skipped this step
                new.set_height(max(new.left.height,new.right.height)+1)
                new.set_size(new.left.size+new.right.size+1)
                




                
        def successor(self,node):
                suc=node
                if node.right.is_real_node()==True:
                        suc=node.right
                        while suc.left.is_real_node()==True:
                                suc=suc.left
                        return suc
                elif suc.parent!=None:
                        p=suc.parent
                        while suc.parent!=None and p.right.is_real_node()==True:
                                if p.right.key==suc.key:
                                        suc=suc.parent
                                        p=suc.parent
                                else:
                                        break
                                                
                        return p
                return None 
                

        """returns an array representing dictionary 

        @rtype: list
        @returns: a sorted list according to key of touples (key, value) representing the data structure
        """
        def avl_to_array(self):
                arr=[]
                x=self.min
                while x!=None:
                        arr+=[(x.key,x.value)]
                        x=self.successor(x)
                return arr


        """returns the number of items in dictionary 

        @rtype: int
        @returns: the number of items in dictionary 
        """
        def size(self):
                return self.root.size       

        
        """splits the dictionary at a given node

        @type node: AVLNode
        @pre: node is in self
        @param node: The intended node in the dictionary according to whom we split
        @rtype: list
        @returns: a list [left, right], where left is an AVLTree representing the keys in the 
        dictionary smaller than node.key, right is an AVLTree representing the keys in the 
        dictionary larger than node.key.
        """
        def split(self, node):
                node=self.search(node.key)
                trees=[]
                P=node.parent
                RT=(node.right).Node2Tree() #the small tree to be
                LT=(node.left).Node2Tree() #the big tree to be
                if P!=None and P.left.key==node.key: #checks whether node is a right or a left child
                        from_left=True
                else:
                        from_left=False
                while P!=None:
                        G=P.parent #Saves the parent of the parent of the node after we split them apart
                        if from_left==False:
                                if G!=None and G.left.key==P.key: #checks whether N is a right or a left child
                                        from_left=True
                                elif G!=None:
                                        from_left=False
                                T2join=(P.left).Node2Tree()
                                if G!=None and from_left:
                                        G.left=AVLNode(None,None)
                                elif G!=None and from_left==False:
                                        G.right=AVLNode(None,None)
                                P.parent=None #to make sure we split P apart
                                LT.join(T2join,P.key,P.value)
                                P=G
                        else:
                                if G!=None and G.left.key==P.key: #checks whether N is a right or a left child
                                        from_left=True
                                elif G!=None:
                                        from_left=False
                                T2join=(P.right).Node2Tree()
                                if G!=None and from_left:
                                        G.left=AVLNode(None,None)
                                elif G!=None and from_left==False:
                                        G.right=AVLNode(None,None)
                                P.parent=None #to make sure we split P apart
                                RT.join(T2join,P.key,P.value)
                                P=G
                        
                                
                
                trees.append(LT)
                trees.append(RT)
                return trees



        
        """joins self with key and another AVLTree

        @type tree: AVLTree 
        @param tree: a dictionary to be joined with self
        @type key: int 
        @param key: The key separting self with tree
        @type val: any 
        @param val: The value attached to key
        @pre: all keys in self are smaller than key and all keys in tree are larger than key,
        or the other way around.
        @rtype: int
        @returns: the absolute value of the difference between the height of the AVL trees joined
        """
        def join(self,tree,key,val):
                node=self.createRealNode(key,val)
                return self.join1(tree,node)
                
        def join1(self,tree,node):      
                if self.root.key==None or self.root.key<node.key:
                        smaller=True
                else:
                        smaller=False
                h1=self.root.height
                h2=tree.root.height
                if smaller==True:#all the keys of self are smaller than all the keys of tree
                        if h1==h2:
                                node.left=self.root
                                node.right=tree.root
                                self.root.parent=node
                                tree.root.parent=node
                                self.root=node
                                res=1
                        elif h1<h2 :#the height of self is smaller than the height of tree
                                if self.root.key==None:#self is empty, we have to save its minimum for later
                                        self.min=node
                                b=tree.root
                                while b.height>h1:
                                        p=b
                                        b=b.left
                                node.right=b
                                if p!=None:
                                        print("hon")
                                        p.left=node
                                node.parent=b.parent
                                b.parent=node
                                node.left=self.root
                                self.root.parent=node
                                self.root=tree.root #changing the root of self to be the root of tree because tree is bigger than self
                                res=h2-h1+1
                                
                        else:
                                b=self.root
                                while b.height>h2:
                                        p=b
                                        b=b.right
                                node.left=b
                                node.parent=b.parent
                                if p!=None:
                                        p.right=node
                                b.parent=node
                                node.right=tree.root
                                tree.root.parent=node
                                res=h1-h2+1
                                
                else:#self.root.key<node.key
                        if h1==h2:
                                node.left=tree.root
                                node.right=self.root
                                self.root.parent=node
                                tree.root.parent=node
                                self.root=node 
                                res=1
                        elif h1<h2:
                                b=tree.root
                                while b.height>h1:
                                        p=b
                                        b=b.right
                                node.left=b
                                node.parent=p
                                if p!=None:
                                        p.right=node
                                b.parent=node
                                node.right=self.root
                                self.root.parent=node
                                self.root=tree.root #changing the root of self to be the root of tree because tree is bigger than self
                                self.min=tree.min
                                res=h2-h1+1
                                
                        else:
                                b=self.root
                                while b.height>h2:
                                        p=b
                                        b=b.left
                                node.right=b
                                node.parent=p
                                if p!=None:
                                        node.parent.left=node
                                b.parent=node
                                node.left=tree.root
                                tree.root.parent=node
                                res=h1-h2+1
                                
                node.set_height(max(node.left.height,node.right.height)+1)
                node.set_size(node.left.size+node.right.size+1)
                self.rebalancing(node)#rebalancing from node upwards if needed
                return res
        
        def rebalancing(self,node):
                R_cnt=0
                while node!=None: 
                        node.set_height(max(node.left.height,node.right.height)+1)
                        node.set_size(node.left.size+node.right.size+1)
                        bf=node.get_BF()
                        if abs(bf)<2:
                                node=node.parent
                        else:
                                if bf==-2:
                                        if node.right.get_BF()==-1 or node.right.get_BF()==0:
                                                self.Left_rotation(node.right,node)
                                                R_cnt+=1
                                                node=node.parent
                                                        
                                        else:
                                                self.Right_rotation(node.right.left,node.right)#(P.left,P)
                                                self.Left_rotation(node.right,node)#(P.parent,P.parent.parent)
                                                R_cnt+=2
                                                node=node.parent
                                                        
                                else:
                                        if node.left.get_BF()==1 or node.left.get_BF()==0:
                                                self.Right_rotation(node.left,node)
                                                R_cnt+=1
                                                node=node.parent
                                        else:
                                                self.Left_rotation(node.left.right,node.left)#(P.right,P)
                                                self.Right_rotation(node.left,node)#(P.parent,P.parent.parent)
                                                R_cnt+=2
                                                node=node.parent
                                                        
                                if node!=None:
                                        node=node.parent
                return None 
                        
                                       
                                
                        
                


        """compute the rank of node in the self

        @type node: AVLNode
        @pre: node is in self
        @param node: a node in the dictionary which we want to compute its rank
        @rtype: int
        @returns: the rank of node in self
        """
        def rank(self, node):
                arr=self.avl_to_array()
                left=0
                root=self.get_root()
                right=root.size-1
                while left<=right:
                        mid=(right+left)//2
                        if arr[mid][0]==node.key:
                                return mid
                        elif arr[mid][0]<node.key:
                                left=mid+1
                        else:
                                right=mid-1
                                
                return None


        """finds the i'th smallest item (according to keys) in self

        @type i: int
        @pre: 1 <= i <= self.size()
        @param i: the rank to be selected in self
        @rtype: int
        @returns: the item of rank i in self
        """
        def select(self, i):
                arr=self.avl_to_array()
                return arr[i]


        """returns the root of the tree representing the dictionary

        @rtype: AVLNode
        @returns: the root, None if the dictionary is empty
        """
        def get_root(self):
                return self.root
