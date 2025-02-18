import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'FlowOfFunds': 1.0
        })
    )
