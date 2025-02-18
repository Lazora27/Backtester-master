import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und PivotPoints
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'PivotPoints': 1.0
        })
    )
