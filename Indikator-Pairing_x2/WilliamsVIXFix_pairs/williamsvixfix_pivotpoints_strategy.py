import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und PivotPoints
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'PivotPoints': 1.0
        })
    )
