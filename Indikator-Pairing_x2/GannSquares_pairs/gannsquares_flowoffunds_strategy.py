import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'FlowOfFunds': 1.0
        })
    )
