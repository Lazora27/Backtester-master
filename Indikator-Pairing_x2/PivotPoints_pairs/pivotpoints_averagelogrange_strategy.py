import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AverageLogRange': 1.0
        })
    )
