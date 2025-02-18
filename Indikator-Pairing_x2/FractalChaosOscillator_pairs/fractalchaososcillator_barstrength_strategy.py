import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und BarStrength
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'BarStrength': 1.0
        })
    )
