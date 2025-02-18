import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
