import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StochasticOscillator': 1.0
        })
    )
