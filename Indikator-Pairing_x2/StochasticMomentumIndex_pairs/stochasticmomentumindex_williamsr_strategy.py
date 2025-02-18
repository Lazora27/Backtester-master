import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
