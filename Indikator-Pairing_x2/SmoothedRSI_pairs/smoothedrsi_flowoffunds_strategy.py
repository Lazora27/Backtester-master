import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FlowOfFunds': 1.0
        })
    )
