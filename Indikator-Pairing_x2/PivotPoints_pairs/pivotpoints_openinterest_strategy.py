import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und OpenInterest
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'OpenInterest': 1.0
        })
    )
