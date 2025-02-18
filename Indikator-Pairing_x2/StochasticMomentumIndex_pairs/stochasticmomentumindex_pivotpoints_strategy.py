import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
