import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
