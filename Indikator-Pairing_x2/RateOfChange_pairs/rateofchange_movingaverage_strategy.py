import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und MovingAverage
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'MovingAverage': 1.0
        })
    )
