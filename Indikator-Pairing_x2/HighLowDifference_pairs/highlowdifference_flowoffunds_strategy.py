import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'FlowOfFunds': 1.0
        })
    )
