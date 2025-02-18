import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_RelativeVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und RelativeVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'RelativeVolatilityIndex': {
                'class': RelativeVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVolatilityIndex'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'RelativeVolatilityIndex': 1.0
        })
    )
