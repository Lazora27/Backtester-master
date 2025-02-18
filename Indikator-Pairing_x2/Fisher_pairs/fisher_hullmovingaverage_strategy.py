import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HullMovingAverage': 1.0
        })
    )
