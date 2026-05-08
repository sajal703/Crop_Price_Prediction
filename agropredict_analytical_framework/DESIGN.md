---
name: AgroPredict Analytical Framework
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#1f6d1a'
  on-secondary: '#ffffff'
  secondary-container: '#a4f792'
  on-secondary-container: '#267320'
  tertiary: '#002d1c'
  on-tertiary: '#ffffff'
  tertiary-container: '#00452e'
  on-tertiary-container: '#75b393'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#a4f792'
  secondary-fixed-dim: '#89da79'
  on-secondary-fixed: '#002201'
  on-secondary-fixed-variant: '#005303'
  tertiary-fixed: '#b1f0ce'
  tertiary-fixed-dim: '#95d4b3'
  on-tertiary-fixed: '#002114'
  on-tertiary-fixed-variant: '#0e5138'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 32px
  gutter: 20px
---

## Brand & Style

The design system is rooted in the intersection of agricultural heritage and cutting-edge data science. The visual language moves away from the "organic" softness of consumer apps toward a high-density, **Corporate/Modern** aesthetic that emphasizes precision and institutional trust. 

The style utilizes a "Structured Informational" approach: every pixel serves a purpose in data interpretation. We employ a mix of flat surfaces with precise, low-contrast borders to define hierarchy, ensuring the user feels in control of complex datasets. The emotional response is one of calm authority—reducing the "noise" of market volatility through organized, rhythmic layouts.

## Colors

The palette is anchored by "Forest Deep" (Primary), a color that evokes stability and growth. We use a range of "Earthy Greens" for functional data representation, reserving the brightest green for positive price movement or high-confidence indicators.

The neutral scale is critical for data density; we use a "Cool Slate" spectrum for backgrounds to reduce eye strain during prolonged analysis. High-contrast chart colors are selected to remain distinct even when multiple crop types are overlaid on a single coordinate plane.

## Typography

This design system utilizes **Manrope** for structural headings to provide a modern, geometric feel that remains professional. For the core data experience, **Inter** is used for its exceptional legibility at small sizes and its neutral "utilitarian" character.

Tabular data and price figures should utilize Inter with specific tracking adjustments to ensure vertical alignment in columns. We prioritize a clear typographic hierarchy where labels are distinct from values to facilitate rapid "scanning" of market dashboards.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid Grid**. Main dashboards use a 12-column system for wide-screen data visualization, while individual metric cards utilize a tight 4px base unit to maximize information density.

We employ "Data Grouping" via spacing; related metrics are kept at 8px (sm) intervals, while distinct analytical modules are separated by 40px (xl) to prevent cognitive overload. Gutters are kept narrow (20px) to allow charts as much horizontal real estate as possible.

## Elevation & Depth

This design system uses **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows. The background is a soft light gray, and primary containers (cards) are pure white with a 1px border in a slightly darker neutral.

To indicate focus or "active" states in the machine learning models, we use a subtle 2px inset stroke of the primary green color. Depth is used sparingly: only the primary "Forecast Action" modals receive an ambient, low-opacity shadow to pull them into the foreground.

## Shapes

The shape language is "Soft Professional." We use a **0.25rem (4px)** base radius for all data inputs and small components to maintain a disciplined, technical appearance. Larger containers like price charts and forecast cards use **0.5rem (8px)** to subtly soften the interface and make it feel more modern and approachable. Pill shapes are reserved exclusively for "Status Tags" (e.g., "High Confidence") to make them instantly recognizable against the rectangular grid of data.

## Components

### Metric Cards
White backgrounds, 1px border (#E9ECEF). The primary value is displayed in 24px Manrope Bold. A "Trend Indicator" chip is placed in the top right, using semantic coloring (Green for up, Red for down).

### High-Contrast Charts
Line charts use a 2px stroke width. The "Predicted" line is dashed to differentiate it from "Historical" solid lines. Tooltips should be dark-themed (#1B4332) with white Inter typography to pop against the light grid.

### Confidence Indicators
A custom component featuring a segmented progress bar (3 levels: Low, Med, High). Each segment fills with the primary green to show the ML model's certainty.

### Buttons & Inputs
Primary buttons are solid Forest Deep (#1B4332) with white text. Input fields use a 1px border and a subtle 4px corner radius. On focus, the border transitions to the primary green with a 2px outer glow of 10% opacity.

### Data Tables
Stripped rows using the neutral background color. Header rows are sticky with a 2px bottom border. Text alignment follows financial standards: labels to the left, numerical values to the right.