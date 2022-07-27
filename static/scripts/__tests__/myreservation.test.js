/**
 * @jest-environment jsdom
 */

const {
    openDeleteConfirmationDialog,
    deleteReservation,
    cancelReservationDeletion} = require("../myreservation");
    
beforeAll(() => {
    let fs = require("fs");
    let fileContents = fs.readFileSync("templates/my/reservation/index.html", "utf-8");
    document.open();
    document.write(fileContents);
    document.close();
});

describe("Cancel reservation tests", () => {

    describe("Click on cancel reservation", () => {
        const modal = jest.fn();
        const jQuery = jest.fn(() => ({
            modal,
        }));
        const event = { preventDefault: () => {} };

        beforeEach(() => {
            jest.spyOn(event, 'preventDefault');
        });

        test("Expects confirmation modal to show", () => {
            openDeleteConfirmationDialog(jQuery, event, "#deleteReservationForm");
            expect(event.preventDefault).toBeCalled();
            expect(modal.mock.calls.length).toBe(1);
        });
    });

    describe("Click on 'Yes' in confirmation modal", () => {
        const modal = jest.fn();
        const submit = jest.fn();
        const jQuery = jest.fn(() => ({
            modal,
            submit
        }));
        test("Expects modal to show", () => {
            deleteReservation(jQuery, "#cancelReservationDialog", '#deleteReservation');
            expect(modal.mock.calls.length).toBe(1);
            expect(submit.mock.calls.length).toBe(1);
        });
    });

    describe("Click on 'No' in confirmation modal", () => {
        const modal = jest.fn();
        const jQuery = jest.fn(() => ({
            modal
        }));
        test("Expects modal to show", () => {
            cancelReservationDeletion(jQuery, "#cancelReservationDialog");
            expect(modal.mock.calls.length).toBe(1);
        });
    });
});
