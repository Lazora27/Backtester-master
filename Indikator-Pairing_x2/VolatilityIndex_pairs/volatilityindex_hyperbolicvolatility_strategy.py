import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
