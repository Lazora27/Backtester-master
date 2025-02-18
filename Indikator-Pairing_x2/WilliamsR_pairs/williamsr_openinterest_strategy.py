import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und OpenInterest
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'OpenInterest': 1.0
        })
    )
