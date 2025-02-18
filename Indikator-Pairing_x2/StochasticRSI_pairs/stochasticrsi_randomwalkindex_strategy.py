import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
