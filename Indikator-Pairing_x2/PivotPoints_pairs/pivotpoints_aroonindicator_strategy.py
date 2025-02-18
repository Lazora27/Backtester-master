import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AroonIndicator': 1.0
        })
    )
