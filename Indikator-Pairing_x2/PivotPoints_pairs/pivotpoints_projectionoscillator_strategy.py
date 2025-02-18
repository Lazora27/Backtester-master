import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
