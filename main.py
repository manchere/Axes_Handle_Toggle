import maya.cmds as cmds

def displayAttr(attrName, attrDisplay=False):
    joint_list = selection()
    for jnt in joint_list:
        cmds.setAttr(jnt + "." + attrName, attrDisplay)


def handleOffset(sliderName, handleName):
    joint_list = selection()
    h_off = cmds.floatSliderGrp(sliderName, q=True, v=True)
    for jnt in joint_list:
        cmds.setAttr(jnt + "." + handleName, h_off)


def selection():
    hier_s = cmds.checkBox('hierSel', q=True, v=True)
    joint_list = []
    if len(cmds.ls(sl=True, type="joint")) == 0:
        joint_list = cmds.ls(type="joint")
    elif hier_s:
        for jnt in cmds.ls(sl=True, type="joint"):
           print(cmds.listRelatives(jnt, ad=True, type='joint'))
           joint_list.extend(cmds.listRelatives(jnt, ad=True, type='joint'))
           joint_list.append(jnt)
    else:
        joint_list = cmds.ls(sl=True, type="joint")
    return joint_list


if cmds.window('Axis_Display', exists=True):
    cmds.deleteUI('Axis_Display')

cmds.window('Axis Display', title='Axis Display', w=150)
cmds.columnLayout(adjustableColumn=True)
cmds.frameLayout(label='Settings', cll=False, bgc=[0, 0.2, 0.3], w=200)
cmds.checkBox('axisDis', label='Display Local Axis')
cmds.checkBox('axisDis', onc=lambda x: displayAttr('displayLocalAxis', True), edit=True)
cmds.checkBox('axisDis', ofc=lambda x: displayAttr('displayLocalAxis', False), edit=True)

cmds.checkBox('hierSel', label='Selection by hierarchy')

cmds.frameLayout(label='Handle Settings', cll=False, bgc=[0, 0.2, 0.3], w=200)

cmds.checkBox('handleDis', label='Display Local Handle')
cmds.checkBox('handleDis', onc=lambda x: displayAttr('displayHandle', True), edit=True)
cmds.checkBox('handleDis', ofc=lambda x: displayAttr('displayHandle', False), edit=True)

cmds.floatSliderGrp('h_offset_x', l='handle offset x', min=-10, max=10, value=0, field=True)
cmds.floatSliderGrp('h_offset_x', e=True, cc=lambda x: handleOffset('h_offset_x', 'selectHandleX'))

cmds.floatSliderGrp('h_offset_y', l='handle offset y', min=-10, max=10, value=0, field=True)
cmds.floatSliderGrp('h_offset_y', e=True, cc=lambda x: handleOffset('h_offset_y', 'selectHandleY'))

cmds.floatSliderGrp('h_offset_z', l='handle offset z', min=-10, max=10, value=0, field=True)
cmds.floatSliderGrp('h_offset_z', e=True, cc=lambda x: handleOffset('h_offset_z', 'selectHandleZ'))
cmds.showWindow()
