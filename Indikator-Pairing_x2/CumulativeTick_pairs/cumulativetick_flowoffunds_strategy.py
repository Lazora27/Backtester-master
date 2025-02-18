import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'FlowOfFunds': 1.0
        })
    )
