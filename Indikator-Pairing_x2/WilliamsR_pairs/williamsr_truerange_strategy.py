import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TrueRange
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TrueRange': 1.0
        })
    )
