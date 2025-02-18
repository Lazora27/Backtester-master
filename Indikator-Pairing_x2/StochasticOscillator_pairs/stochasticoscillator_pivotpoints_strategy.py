import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'PivotPoints': 1.0
        })
    )
