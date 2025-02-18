import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und MovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'MovingAverage': 1.0
        })
    )
