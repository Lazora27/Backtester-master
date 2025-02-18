import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FractalChaosOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FractalChaosOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FractalChaosOscillator': 1.0
        })
    )
