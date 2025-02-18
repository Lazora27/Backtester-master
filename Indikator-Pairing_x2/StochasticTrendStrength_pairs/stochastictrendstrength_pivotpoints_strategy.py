import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'PivotPoints': 1.0
        })
    )
