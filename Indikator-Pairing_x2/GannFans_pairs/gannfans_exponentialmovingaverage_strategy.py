import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
