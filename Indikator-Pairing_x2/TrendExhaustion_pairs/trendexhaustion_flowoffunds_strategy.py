import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FlowOfFunds': 1.0
        })
    )
