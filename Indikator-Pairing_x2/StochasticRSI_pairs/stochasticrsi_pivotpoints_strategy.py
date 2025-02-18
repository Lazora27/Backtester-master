import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und PivotPoints
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'PivotPoints': 1.0
        })
    )
