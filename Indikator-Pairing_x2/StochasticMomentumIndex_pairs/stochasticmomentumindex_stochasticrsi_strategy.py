import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'StochasticRSI': 1.0
        })
    )
