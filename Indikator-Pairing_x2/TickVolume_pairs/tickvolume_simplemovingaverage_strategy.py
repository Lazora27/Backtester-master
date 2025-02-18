import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
