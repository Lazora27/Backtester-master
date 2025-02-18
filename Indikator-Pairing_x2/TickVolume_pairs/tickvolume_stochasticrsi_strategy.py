import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'StochasticRSI': 1.0
        })
    )
