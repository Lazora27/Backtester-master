import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PivotPoints
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PivotPoints': 1.0
        })
    )
