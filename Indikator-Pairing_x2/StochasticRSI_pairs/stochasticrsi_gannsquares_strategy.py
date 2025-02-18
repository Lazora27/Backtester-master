import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und GannSquares
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'GannSquares': 1.0
        })
    )
