import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
