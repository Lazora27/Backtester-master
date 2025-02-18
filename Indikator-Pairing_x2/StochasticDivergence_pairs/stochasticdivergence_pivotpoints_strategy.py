import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'PivotPoints': 1.0
        })
    )
