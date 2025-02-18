import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
