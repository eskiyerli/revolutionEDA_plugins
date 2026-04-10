# RevEDA Simulation Plugin

RevEDA Simulation (revedasim) is a comprehensive circuit simulation plugin for Revolution
EDA that provides seamless integration with the Xyce circuit simulator. It enables users to
perform various circuit analyses including DC, AC, transient, noise, and harmonic balance
simulations directly from the schematic editor, with support for multi-dimensional parameter
sweeps and automatic result visualization through the integrated plotting system.

## Features

### Simulation Capabilities

- **Xyce Simulator Integration**: Full support for Sandia National Labs' Xyce circuit
  simulator
- **Multiple Analysis Types**: DC, AC, transient, noise, and harmonic balance analyses
- **Parameter Sweeps**: Multi-dimensional parameter sweep capabilities with nested loops
- **Netlist Generation**: Automatic SPICE netlist generation from Revolution EDA schematics
- **Model Library Support**: Integration with SPICE model libraries and include files

### Analysis Configuration

- **Interactive Setup**: Graphical interface for configuring simulation parameters
- **Analysis Management**: Enable/disable multiple analyses in a single simulation run
- **Output Selection**: Flexible selection of nodes, currents, and expressions to save
- **Initial Conditions**: Support for .IC and .NODESET statements
- **Simulation Options**: Comprehensive control over solver parameters and tolerances

### Parameter Management

- **Variable Definition**: Define simulation parameters with ranges and lists
- **Sweep Syntax**: Support for start:stop:step and comma-separated value lists
- **Parameter Validation**: Automatic checking of parameter names and values
- **Dynamic Netlisting**: Parameters are properly substituted in generated netlists

### Process Management

- **Background Execution**: Non-blocking simulation execution with progress monitoring
- **Multiple Jobs**: Concurrent execution of different analysis types
- **Error Handling**: Comprehensive error reporting and logging
- **File Management**: Automatic organization of simulation files and results

### Integration Features

- **Plugin Architecture**: Seamless integration with Revolution EDA's plugin system
- **Plot Integration**: Automatic launching and data transfer to revedaPlot plugin
- **Model Validation**: Parameter name validation against reserved SPICE keywords
- **Configuration Persistence**: Save and restore simulation settings

## Supported Analysis Types

### DC Analysis

- Linear and logarithmic sweeps
- Voltage and current source sweeps
- Parameter sweeps with nested loops
- Operating point analysis with save options

### AC Analysis

- Linear, octave, and decade frequency sweeps
- Small-signal frequency response
- Complex impedance and admittance calculations

### Transient Analysis

- Time-domain simulation with configurable time steps
- Initial condition support (UIC option)
- Scheduled analysis with time-based events
- Multiple integration methods and tolerances

### Noise Analysis

- Input-referred and output noise calculations
- Frequency-dependent noise analysis
- Support for multiple noise sources

### Harmonic Balance

- Steady-state analysis for nonlinear circuits
- Multi-tone analysis capabilities
- Configurable frequency points and harmonics

## Installation and Usage

The revedasim plugin is automatically loaded when Revolution EDA starts. Access simulation
features through:

1. **Simulation Menu**: Configure analyses and parameters
2. **Simulation Panel**: Monitor running simulations
3. **Output Selection**: Choose signals to plot and analyze
4. **Results Viewer**: Integrated plotting and data analysis

## Requirements

- Revolution EDA core application
- Xyce circuit simulator (version 7.0 or later recommended)
- revedaPlot plugin for result visualization
- Python packages: polars, numpy, quantiphy

## Configuration

Simulation settings can be configured through:

- Environment variables (e.g., REVEDA_VA_MODULE_PATH)
- Configuration files for persistent settings
- Per-project simulation parameters
- Global solver options and tolerances