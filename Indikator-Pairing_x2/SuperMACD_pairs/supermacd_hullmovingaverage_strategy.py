import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HullMovingAverage': 1.0
        })
    )
