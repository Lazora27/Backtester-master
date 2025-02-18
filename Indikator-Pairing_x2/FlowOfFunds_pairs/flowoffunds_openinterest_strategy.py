import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und OpenInterest
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'OpenInterest': 1.0
        })
    )
