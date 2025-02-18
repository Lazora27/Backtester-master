import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'BollingerPercentB': 1.0
        })
    )
