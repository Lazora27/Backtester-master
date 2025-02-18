import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'FlowOfFunds': 1.0
        })
    )
