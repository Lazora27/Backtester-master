import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ProjectionBands': 1.0
        })
    )
