import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'BollingerPercentB': 1.0
        })
    )
