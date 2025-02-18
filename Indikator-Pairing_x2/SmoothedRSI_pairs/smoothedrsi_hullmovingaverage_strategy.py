import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HullMovingAverage': 1.0
        })
    )
