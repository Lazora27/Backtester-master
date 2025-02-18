import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
