import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
