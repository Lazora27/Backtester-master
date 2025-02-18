import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
