# 🗑️ How to Remove Ubuntu from a Windows 10 Dual-Boot System

This guide walks you through the **safe removal of Ubuntu Linux** from a dual-boot setup with **Windows 10**, restoring your system to boot directly into Windows.

---

## ⚠️ Important Notice

> 💡 **Back up your important data** before making changes to system partitions or bootloaders. Proceed with caution.

---

## ✅ Requirements

- Admin access to your Windows 10 system
- Basic understanding of disk partitions and boot menus

---

## 🧰 Steps to Remove Ubuntu Safely

### 1. **Delete Ubuntu Partitions**

1. Press `Windows + X` and choose **Disk Management**.
2. Locate the **Ubuntu partitions**:
   - Typically labeled as “Healthy (Primary Partition)” or “EXT4” with no drive letter.
   - May also have a “swap” partition.
3. Right-click each Ubuntu-related partition and select **Delete Volume**.
4. After deletion, the space becomes **Unallocated**.
5. (Optional) Right-click your main Windows partition and choose **Extend Volume** to reclaim the space.

---


### 2. **Removing Ubuntu from Boot Configuration Data**

#### Use Command Prompt

1. Boot into **Windows**.
2. Open **Command Prompt as Administrator**.
3. Run the following command:

  > bcdedit /enum firmware

4. Find the identifier tag for Ubuntu (Format: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx})

5. Run the command:

  > bcdedit /delete  {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}



--- 

### 3. **Removing Ubuntu from EFI partition**

Ubuntu uses **GRUB** as the bootloader. You’ll need to remove it and restore the default Windows boot manager.

#### Use Command Prompt

1. Boot into **Windows**.
2. Open **Command Prompt as Administrator**.
3. Run the following command:

  > diskpart
  > list disk

4. Select disk that contains EFI partition (X is the id-number of disk)

  > sel disk X

5. List volumes

  > list vol

6. Select volume that contains EFI partition, usually a 100MB Info: System (X is the id-number of volume)

  > sel vol X

7. Assign volume to an unused drive letter, then exit diskpart
   
  > assign letter=Z
  > exit

8. Navigate to EFI folder and delete Ubuntu

  > dir
  > cd EFI
  > dir 
  > rmdir /s ubuntu

