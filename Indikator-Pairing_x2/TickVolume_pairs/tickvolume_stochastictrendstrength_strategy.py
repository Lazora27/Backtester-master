import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
