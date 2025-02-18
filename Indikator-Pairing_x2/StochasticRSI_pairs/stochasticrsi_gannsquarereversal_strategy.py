import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'GannSquareReversal': 1.0
        })
    )
