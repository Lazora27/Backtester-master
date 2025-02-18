import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
