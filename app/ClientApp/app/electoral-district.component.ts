import { Component, Input, Output } from '@angular/core'
import { Region } from './region.model'
import { RegionService } from './region.service'
import { StateService } from './state.service'

@Component({
    selector: 'electoral-district',
    template: `
        <table *ngFor="let region of regions">
            <tr>
                <th> {{  }}</th>
            </tr>
        </table>
    `
})

export class ElectoralDistrictComponent {
    @Input('id') id: number
    Regions: Region[] = [];

    constructor() { }
}