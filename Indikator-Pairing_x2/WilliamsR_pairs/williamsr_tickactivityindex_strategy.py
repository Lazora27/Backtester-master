import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'TickActivityIndex': 1.0
        })
    )
