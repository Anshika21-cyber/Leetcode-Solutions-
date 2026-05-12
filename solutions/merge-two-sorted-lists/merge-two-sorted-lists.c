/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode dummy;
    struct ListNode* list3=&dummy;
    list3->next=NULL;
    while( list1!=NULL && list2!= NULL){
            if (list1->val <= list2->val){
                list3->next=list1;
                list1=list1->next;
            }
            else {
                list3->next=list2;
                list2=list2->next;
            }
            list3=list3->next;
    }
    if (list1!= NULL){
        list3->next=list1;
        list1=list1->next;
    }
        
    else if (list2!=NULL){
        list3->next=list2;
        list2=list2->next;
    }

     return dummy.next;
}