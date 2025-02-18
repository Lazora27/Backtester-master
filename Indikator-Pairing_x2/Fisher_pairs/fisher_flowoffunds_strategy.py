import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'FlowOfFunds': 1.0
        })
    )
