import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'FlowOfFunds': 1.0
        })
    )
