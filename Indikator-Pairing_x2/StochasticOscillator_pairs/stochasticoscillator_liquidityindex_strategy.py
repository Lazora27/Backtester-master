import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'LiquidityIndex': 1.0
        })
    )
