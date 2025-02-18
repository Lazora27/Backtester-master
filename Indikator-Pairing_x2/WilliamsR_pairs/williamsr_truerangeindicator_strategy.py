import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
