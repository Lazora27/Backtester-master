import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'FlowOfFunds': 1.0
        })
    )
