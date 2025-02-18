import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'LiquidityIndex': 1.0
        })
    )
