import { modelActions, modelSelectors } from 'ducks/basemodel'
export const MODEL = 'frontpage'
export const actions = modelActions(MODEL)
export const selectors = modelSelectors(MODEL)

export const fields = {
  id: {
    label: 'ID',
    type: 'integer',
    required: false,
    editable: false,
  },
  headline: {
    label: 'tittel',
    type: 'shorttext',
    required: false,
    editable: true,
    helpText: 'tittel / overskrift',
    maxLength: 200,
  },
  kicker: {
    label: 'stikktittel',
    type: 'string',
    required: false,
    editable: true,
    helpText: 'stikktittel',
    maxLength: 200,
  },
  vignette: {
    label: 'vignett',
    type: 'string',
    required: false,
    editable: true,
    helpText: 'vignett',
    maxLength: 50,
  },
  lede: {
    label: 'ingress',
    type: 'shorttext',
    required: false,
    editable: true,
    helpText: 'ingress',
    maxLength: 200,
  },
  html_class: {
    type: 'string',
    required: false,
    editable: true,
    label: 'Html class',
    helpText: 'html class',
    maxLength: 200,
  },
  priority: {
    label: 'prioritet',
    type: 'range',
    step: 0.1,
    min: -20,
    max: 20,
    editable: true,
  },
  columns: {
    label: 'kolonner',
    type: 'select',
    required: true,
    editable: true,
    helpText: 'base width',
    options: [
      { value: 2, label: '2' },
      { value: 3, label: '3' },
      { value: 4, label: '4' },
      { value: 6, label: '6' },
    ],
  },
  rows: {
    label: 'rader',
    type: 'select',
    required: true,
    editable: true,
    helpText: 'base height',
    options: [
      { value: 1, label: '1' },
      { value: 2, label: '2' },
      { value: 3, label: '3' },
      { value: 4, label: '4' },
      { value: 5, label: '5' },
      { value: 6, label: '6' },
    ],
  },
  published: {
    label: 'publisert',
    type: 'boolean',
    required: false,
    editable: true,
    helpText: 'published',
  },
  imagefile: {
    label: 'foto',
    type: 'select',
    to: 'photos',
    required: false,
    editable: true,
  },
  image: {
    type: 'thumb',
    required: false,
    editable: false,
  },
  crop_box: {
    label: 'beskjæring',
    type: 'field',
    required: false,
    editable: false,
  },
  section: {
    label: 'seksjon',
    type: 'integer',
    required: false,
    editable: false,
  },
  language: {
    label: 'språk',
    type: 'field',
    required: false,
    editable: false,
  },
  story: {
    label: 'artikkel',
    type: 'select',
    to: 'stories',
    editable: false,
  },
}