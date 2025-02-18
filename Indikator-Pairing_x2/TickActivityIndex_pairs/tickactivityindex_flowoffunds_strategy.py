import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
