import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
