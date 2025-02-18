import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FlowOfFunds': 1.0
        })
    )
