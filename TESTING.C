#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

/* Structure to store nurse information */
struct Nurse {
    int nurseId;
    char name[50];
    char gender[10];        /* Male/Female */
    char type[20];          /* Registered/Physiotherapist */
    char category[15];      /* Regular/Third Party */
    float hourlyRate;
    int available;          /* 1 = Available, 0 = Booked */
};

/* Structure to store booking information */
struct Booking {
    int bookingId;
    int nurseId;
    char patientName[50];
    char patientContact[15];
    int hours;
    float totalAmount;
    int billPaid;           /* 1 = Paid, 0 = Unpaid */
    char bookingDate[15];
};

/* Global arrays and counters */
struct Nurse nurses[100];
struct Booking bookings[100];
int nurseCount = 0;
int bookingCount = 0;

/* Function declarations */
void initializeNurses(void);
void mainMenu(void);
void addNurse(void);
void viewNurses(void);
void bookNurse(void);
void viewBookings(void);
void updatePaymentStatus(void);
void searchNurse(void);
void availableNurses(void);
void generateBill(void);
void nurseStatistics(void);

int main() {
    clrscr();
    initializeNurses();
    
    printf("\n\t\t===============================================");
    printf("\n\t\t          NURSE BOOKING MANAGEMENT SYSTEM     ");
    printf("\n\t\t===============================================");
    printf("\n\n\t\tPress any key to continue...");
    getch();
    
    mainMenu();
    return 0;
}

void initializeNurses(void) {
    /* Initialize with some sample nurses */
    strcpy(nurses[0].name, "Sarah Johnson");
    strcpy(nurses[0].gender, "Female");
    strcpy(nurses[0].type, "Registered");
    strcpy(nurses[0].category, "Regular");
    nurses[0].nurseId = 1001;
    nurses[0].hourlyRate = 25.0;
    nurses[0].available = 1;
    
    strcpy(nurses[1].name, "Michael Smith");
    strcpy(nurses[1].gender, "Male");
    strcpy(nurses[1].type, "Physiotherapist");
    strcpy(nurses[1].category, "Third Party");
    nurses[1].nurseId = 1002;
    nurses[1].hourlyRate = 35.0;
    nurses[1].available = 1;
    
    strcpy(nurses[2].name, "Emily Davis");
    strcpy(nurses[2].gender, "Female");
    strcpy(nurses[2].type, "Registered");
    strcpy(nurses[2].category, "Third Party");
    nurses[2].nurseId = 1003;
    nurses[2].hourlyRate = 30.0;
    nurses[2].available = 1;
    
    strcpy(nurses[3].name, "Robert Wilson");
    strcpy(nurses[3].gender, "Male");
    strcpy(nurses[3].type, "Physiotherapist");
    strcpy(nurses[3].category, "Regular");
    nurses[3].nurseId = 1004;
    nurses[3].hourlyRate = 28.0;
    nurses[3].available = 1;
    
    nurseCount = 4;
}

void mainMenu(void) {
    int choice;
    
    while(1) {
        clrscr();
        printf("\n\t\t===============================================");
        printf("\n\t\t          NURSE BOOKING MANAGEMENT SYSTEM     ");
        printf("\n\t\t===============================================");
        printf("\n\n\t\t1. Add New Nurse");
        printf("\n\t\t2. View All Nurses");
        printf("\n\t\t3. Book a Nurse");
        printf("\n\t\t4. View All Bookings");
        printf("\n\t\t5. Update Payment Status");
        printf("\n\t\t6. Search Nurse");
        printf("\n\t\t7. View Available Nurses");
        printf("\n\t\t8. Generate Bill");
        printf("\n\t\t9. Nurse Statistics");
        printf("\n\t\t0. Exit");
        printf("\n\n\t\tEnter your choice: ");
        scanf("%d", &choice);
        
        switch(choice) {
            case 1: addNurse(); break;
            case 2: viewNurses(); break;
            case 3: bookNurse(); break;
            case 4: viewBookings(); break;
            case 5: updatePaymentStatus(); break;
            case 6: searchNurse(); break;
            case 7: availableNurses(); break;
            case 8: generateBill(); break;
            case 9: nurseStatistics(); break;
            case 0: 
                printf("\n\n\t\tThank you for using Nurse Booking System!");
                printf("\n\t\tPress any key to exit...");
                getch();
                exit(0);
            default:
                printf("\n\n\t\tInvalid choice! Press any key to continue...");
                getch();
        }
    }
}

void addNurse(void) {
    int genderChoice, typeChoice, categoryChoice;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t                ADD NEW NURSE                 ");
    printf("\n\t\t===============================================");
    
    if(nurseCount >= 100) {
        printf("\n\n\t\tMaximum nurse limit reached!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    nurses[nurseCount].nurseId = 1001 + nurseCount;
    
    printf("\n\n\t\tNurse ID: %d", nurses[nurseCount].nurseId);
    printf("\n\t\tEnter Nurse Name: ");
    fflush(stdin);
    gets(nurses[nurseCount].name);
    
    printf("\n\t\tSelect Gender:");
    printf("\n\t\t1. Male");
    printf("\n\t\t2. Female");
    printf("\n\t\tChoice: ");
    scanf("%d", &genderChoice);
    if(genderChoice == 1)
        strcpy(nurses[nurseCount].gender, "Male");
    else
        strcpy(nurses[nurseCount].gender, "Female");
    
    printf("\n\t\tSelect Nurse Type:");
    printf("\n\t\t1. Registered Nurse");
    printf("\n\t\t2. Physiotherapist");
    printf("\n\t\tChoice: ");
    scanf("%d", &typeChoice);
    if(typeChoice == 1)
        strcpy(nurses[nurseCount].type, "Registered");
    else
        strcpy(nurses[nurseCount].type, "Physiotherapist");
    
    printf("\n\t\tSelect Category:");
    printf("\n\t\t1. Regular");
    printf("\n\t\t2. Third Party");
    printf("\n\t\tChoice: ");
    scanf("%d", &categoryChoice);
    if(categoryChoice == 1)
        strcpy(nurses[nurseCount].category, "Regular");
    else
        strcpy(nurses[nurseCount].category, "Third Party");
    
    printf("\n\t\tEnter Hourly Rate ($): ");
    scanf("%f", &nurses[nurseCount].hourlyRate);
    
    nurses[nurseCount].available = 1;
    nurseCount++;
    
    printf("\n\n\t\tNurse added successfully!");
    printf("\n\t\tPress any key to continue...");
    getch();
}

void viewNurses(void) {
    int i;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t                ALL NURSES                    ");
    printf("\n\t\t===============================================");
    
    if(nurseCount == 0) {
        printf("\n\n\t\tNo nurses found!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    printf("\n\nID    Name                 Gender  Type           Category     Rate   Status");
    printf("\n---------------------------------------------------------------------------");
    
    for(i = 0; i < nurseCount; i++) {
        printf("\n%-6d%-20s %-8s%-15s %-12s%-8.2f%s",
               nurses[i].nurseId,
               nurses[i].name,
               nurses[i].gender,
               nurses[i].type,
               nurses[i].category,
               nurses[i].hourlyRate,
               nurses[i].available ? "Available" : "Booked");
    }
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}

void bookNurse(void) {
    int selectedNurseId, nurseIndex = -1;
    int availableCount = 0;
    int i, j;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t                BOOK A NURSE                  ");
    printf("\n\t\t===============================================");
    
    if(nurseCount == 0) {
        printf("\n\n\t\tNo nurses available for booking!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    /* Show available nurses */
    printf("\n\n\t\tAvailable Nurses:");
    printf("\n\nID    Name                 Gender  Type           Category     Rate");
    printf("\n--------------------------------------------------------------------");
    
    for(i = 0; i < nurseCount; i++) {
        if(nurses[i].available) {
            printf("\n%-6d%-20s %-8s%-15s %-12s%.2f",
                   nurses[i].nurseId,
                   nurses[i].name,
                   nurses[i].gender,
                   nurses[i].type,
                   nurses[i].category,
                   nurses[i].hourlyRate);
            availableCount++;
        }
    }
    
    if(availableCount == 0) {
        printf("\n\n\t\tNo nurses currently available!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    printf("\n\n\t\tEnter Nurse ID to book: ");
    scanf("%d", &selectedNurseId);
    
    /* Find nurse */
    for(i = 0; i < nurseCount; i++) {
        if(nurses[i].nurseId == selectedNurseId && nurses[i].available) {
            nurseIndex = i;
            break;
        }
    }
    
    if(nurseIndex == -1) {
        printf("\n\n\t\tInvalid Nurse ID or Nurse not available!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    /* Get booking details */
    bookings[bookingCount].bookingId = 2001 + bookingCount;
    bookings[bookingCount].nurseId = selectedNurseId;
    
    printf("\n\t\tBooking ID: %d", bookings[bookingCount].bookingId);
    printf("\n\t\tEnter Patient Name: ");
    fflush(stdin);
    gets(bookings[bookingCount].patientName);
    
    printf("\n\t\tEnter Patient Contact: ");
    gets(bookings[bookingCount].patientContact);
    
    printf("\n\t\tEnter Number of Hours: ");
    scanf("%d", &bookings[bookingCount].hours);
    
    printf("\n\t\tEnter Booking Date (DD/MM/YYYY): ");
    fflush(stdin);
    gets(bookings[bookingCount].bookingDate);
    
    bookings[bookingCount].totalAmount = nurses[nurseIndex].hourlyRate * bookings[bookingCount].hours;
    bookings[bookingCount].billPaid = 0;
    
    /* Mark nurse as booked */
    nurses[nurseIndex].available = 0;
    
    bookingCount++;
    
    printf("\n\n\t\t===============================================");
    printf("\n\t\t              BOOKING CONFIRMED               ");
    printf("\n\t\t===============================================");
    printf("\n\t\tBooking ID: %d", bookings[bookingCount-1].bookingId);
    printf("\n\t\tNurse: %s", nurses[nurseIndex].name);
    printf("\n\t\tPatient: %s", bookings[bookingCount-1].patientName);
    printf("\n\t\tHours: %d", bookings[bookingCount-1].hours);
    printf("\n\t\tTotal Amount: $%.2f", bookings[bookingCount-1].totalAmount);
    printf("\n\t\tPayment Status: Unpaid");
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}

void viewBookings(void) {
    int i;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t              ALL BOOKINGS                    ");
    printf("\n\t\t===============================================");
    
    if(bookingCount == 0) {
        printf("\n\n\t\tNo bookings found!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    printf("\nBookID NurseID Patient              Contact        Hours Amount   Date       Payment");
    printf("\n---------------------------------------------------------------------------------");
    
    for(i = 0; i < bookingCount; i++) {
        printf("\n%-6d %-7d %-20s %-14s %-5d %-8.2f %-10s %s",
               bookings[i].bookingId,
               bookings[i].nurseId,
               bookings[i].patientName,
               bookings[i].patientContact,
               bookings[i].hours,
               bookings[i].totalAmount,
               bookings[i].bookingDate,
               bookings[i].billPaid ? "Paid" : "Unpaid");
    }
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}

void updatePaymentStatus(void) {
    int bookingId;
    int unpaidCount = 0;
    int i, j;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t           UPDATE PAYMENT STATUS              ");
    printf("\n\t\t===============================================");
    
    if(bookingCount == 0) {
        printf("\n\n\t\tNo bookings found!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    /* Show unpaid bookings */
    printf("\n\n\t\tUnpaid Bookings:");
    printf("\nBookID NurseID Patient              Amount   Date");
    printf("\n-------------------------------------------------------");
    
    for(i = 0; i < bookingCount; i++) {
        if(!bookings[i].billPaid) {
            printf("\n%-6d %-7d %-20s %-8.2f %s",
                   bookings[i].bookingId,
                   bookings[i].nurseId,
                   bookings[i].patientName,
                   bookings[i].totalAmount,
                   bookings[i].bookingDate);
            unpaidCount++;
        }
    }
    
    if(unpaidCount == 0) {
        printf("\n\n\t\tAll bills are paid!");
        printf("\n\t\tPress any key to continue...");
        getch();
        return;
    }
    
    printf("\n\n\t\tEnter Booking ID to mark as paid: ");
    scanf("%d", &bookingId);
    
    for(i = 0; i < bookingCount; i++) {
        if(bookings[i].bookingId == bookingId && !bookings[i].billPaid) {
            bookings[i].billPaid = 1;
            
            /* Make nurse available again */
            for(j = 0; j < nurseCount; j++) {
                if(nurses[j].nurseId == bookings[i].nurseId) {
                    nurses[j].available = 1;
                    break;
                }
            }
            
            printf("\n\n\t\tPayment status updated successfully!");
            printf("\n\t\tNurse is now available for new bookings.");
            printf("\n\t\tPress any key to continue...");
            getch();
            return;
        }
    }
    
    printf("\n\n\t\tInvalid Booking ID or bill already paid!");
    printf("\n\t\tPress any key to continue...");
    getch();
}

void searchNurse(void) {
    int choice;
    char searchTerm[50];
    int found = 0;
    int i;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t              SEARCH NURSE                    ");
    printf("\n\t\t===============================================");
    
    printf("\n\n\t\tSearch by:");
    printf("\n\t\t1. Gender (Male/Female)");
    printf("\n\t\t2. Type (Registered/Physiotherapist)");
    printf("\n\t\t3. Category (Regular/Third Party)");
    printf("\n\n\t\tEnter choice: ");
    
    scanf("%d", &choice);
    
    printf("\n\t\tEnter search term: ");
    fflush(stdin);
    gets(searchTerm);
    
    printf("\n\n\t\tSearch Results:");
    printf("\nID    Name                 Gender  Type           Category     Rate   Status");
    printf("\n---------------------------------------------------------------------------");
    
    for(i = 0; i < nurseCount; i++) {
        int match = 0;
        
        switch(choice) {
            case 1: match = (strcmp(nurses[i].gender, searchTerm) == 0); break;
            case 2: match = (strcmp(nurses[i].type, searchTerm) == 0); break;
            case 3: match = (strcmp(nurses[i].category, searchTerm) == 0); break;
        }
        
        if(match) {
            printf("\n%-6d%-20s %-8s%-15s %-12s%-8.2f%s",
                   nurses[i].nurseId,
                   nurses[i].name,
                   nurses[i].gender,
                   nurses[i].type,
                   nurses[i].category,
                   nurses[i].hourlyRate,
                   nurses[i].available ? "Available" : "Booked");
            found = 1;
        }
    }
    
    if(!found) {
        printf("\n\n\t\tNo nurses found matching your criteria!");
    }
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}

void availableNurses(void) {
    int availableCount = 0;
    int i;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t            AVAILABLE NURSES                  ");
    printf("\n\t\t===============================================");
    
    printf("\n\nID    Name                 Gender  Type           Category     Rate");
    printf("\n--------------------------------------------------------------------");
    
    for(i = 0; i < nurseCount; i++) {
        if(nurses[i].available) {
            printf("\n%-6d%-20s %-8s%-15s %-12s%.2f",
                   nurses[i].nurseId,
                   nurses[i].name,
                   nurses[i].gender,
                   nurses[i].type,
                   nurses[i].category,
                   nurses[i].hourlyRate);
            availableCount++;
        }
    }
    
    if(availableCount == 0) {
        printf("\n\n\t\tNo nurses currently available!");
    } else {
        printf("\n\n\t\tTotal Available Nurses: %d", availableCount);
    }
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}

void generateBill(void) {
    int bookingId;
    int i, j;
    char nurseName[50];
    float hourlyRate;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t              GENERATE BILL                   ");
    printf("\n\t\t===============================================");
    
    printf("\n\n\t\tEnter Booking ID: ");
    scanf("%d", &bookingId);
    
    for(i = 0; i < bookingCount; i++) {
        if(bookings[i].bookingId == bookingId) {
            /* Find nurse details */
            for(j = 0; j < nurseCount; j++) {
                if(nurses[j].nurseId == bookings[i].nurseId) {
                    strcpy(nurseName, nurses[j].name);
                    hourlyRate = nurses[j].hourlyRate;
                    break;
                }
            }
            
            printf("\n\n\t\t===============================================");
            printf("\n\t\t                    BILL                      ");
            printf("\n\t\t===============================================");
            printf("\n\t\tBooking ID      : %d", bookings[i].bookingId);
            printf("\n\t\tDate            : %s", bookings[i].bookingDate);
            printf("\n\t\tPatient Name    : %s", bookings[i].patientName);
            printf("\n\t\tContact         : %s", bookings[i].patientContact);
            printf("\n\t\tNurse Name      : %s", nurseName);
            printf("\n\t\tHours Booked    : %d", bookings[i].hours);
            printf("\n\t\tHourly Rate     : $%.2f", hourlyRate);
            printf("\n\t\t                  --------");
            printf("\n\t\tTotal Amount    : $%.2f", bookings[i].totalAmount);
            printf("\n\t\tPayment Status  : %s", bookings[i].billPaid ? "PAID" : "UNPAID");
            printf("\n\t\t===============================================");
            
            printf("\n\n\t\tPress any key to continue...");
            getch();
            return;
        }
    }
    
    printf("\n\n\t\tBooking ID not found!");
    printf("\n\t\tPress any key to continue...");
    getch();
}

void nurseStatistics(void) {
    int maleCount = 0, femaleCount = 0;
    int registeredCount = 0, physioCount = 0;
    int regularCount = 0, thirdPartyCount = 0;
    int availableCount = 0, bookedCount = 0;
    float totalRevenue = 0;
    int paidBookings = 0, unpaidBookings = 0;
    int i;
    
    clrscr();
    printf("\n\t\t===============================================");
    printf("\n\t\t             NURSE STATISTICS                 ");
    printf("\n\t\t===============================================");
    
    for(i = 0; i < nurseCount; i++) {
        if(strcmp(nurses[i].gender, "Male") == 0) maleCount++;
        else femaleCount++;
        
        if(strcmp(nurses[i].type, "Registered") == 0) registeredCount++;
        else physioCount++;
        
        if(strcmp(nurses[i].category, "Regular") == 0) regularCount++;
        else thirdPartyCount++;
        
        if(nurses[i].available) availableCount++;
        else bookedCount++;
    }
    
    for(i = 0; i < bookingCount; i++) {
        if(bookings[i].billPaid) {
            paidBookings++;
            totalRevenue += bookings[i].totalAmount;
        } else {
            unpaidBookings++;
        }
    }
    
    printf("\n\n\t\tNURSE DEMOGRAPHICS:");
    printf("\n\t\t-------------------");
    printf("\n\t\tTotal Nurses    : %d", nurseCount);
    printf("\n\t\tMale Nurses     : %d", maleCount);
    printf("\n\t\tFemale Nurses   : %d", femaleCount);
    printf("\n\t\tRegistered      : %d", registeredCount);
    printf("\n\t\tPhysiotherapist : %d", physioCount);
    printf("\n\t\tRegular Staff   : %d", regularCount);
    printf("\n\t\tThird Party     : %d", thirdPartyCount);
    
    printf("\n\n\t\tAVAILABILITY STATUS:");
    printf("\n\t\t-------------------");
    printf("\n\t\tAvailable       : %d", availableCount);
    printf("\n\t\tCurrently Booked: %d", bookedCount);
    
    printf("\n\n\t\tBOOKING STATISTICS:");
    printf("\n\t\t-------------------");
    printf("\n\t\tTotal Bookings  : %d", bookingCount);
    printf("\n\t\tPaid Bookings   : %d", paidBookings);
    printf("\n\t\tUnpaid Bookings : %d", unpaidBookings);
    printf("\n\t\tTotal Revenue   : $%.2f", totalRevenue);
    
    printf("\n\n\t\tPress any key to continue...");
    getch();
}