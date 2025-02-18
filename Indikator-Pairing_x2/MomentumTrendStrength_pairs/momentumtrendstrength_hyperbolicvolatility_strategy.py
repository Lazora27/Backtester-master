import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
