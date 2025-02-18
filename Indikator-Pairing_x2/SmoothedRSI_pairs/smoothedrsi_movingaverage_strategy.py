import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und MovingAverage
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'MovingAverage': 1.0
        })
    )
