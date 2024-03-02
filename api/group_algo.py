from products.models import Group, StudentGroup


def add_user_to_group(student, product):
    groups_for_product = Group.objects.filter(product=product)
    max_order = groups_for_product.count()
    for group in groups_for_product:
        if group.students.count() < product.max_group_size:
            StudentGroup.objects.create(student=student, group=group)
            return
    new_group_order = max_order + 1
    new_group = Group.objects.create(product=product, name=f'Group {new_group_order} for {product}')
    StudentGroup.objects.create(student=student, group=new_group)