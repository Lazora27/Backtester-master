import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'FlowOfFunds': 1.0
        })
    )
