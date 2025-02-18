import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HullMovingAverage': 1.0
        })
    )
