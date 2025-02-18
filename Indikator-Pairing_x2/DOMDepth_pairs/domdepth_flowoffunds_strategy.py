import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'FlowOfFunds': 1.0
        })
    )
