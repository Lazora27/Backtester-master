import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
