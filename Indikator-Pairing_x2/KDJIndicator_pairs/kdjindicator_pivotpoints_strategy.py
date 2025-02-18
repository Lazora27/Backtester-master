import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'PivotPoints': 1.0
        })
    )
