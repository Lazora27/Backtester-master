import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'LiquidityIndex': 1.0
        })
    )
