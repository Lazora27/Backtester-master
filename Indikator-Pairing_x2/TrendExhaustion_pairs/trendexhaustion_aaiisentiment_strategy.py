import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AAIISentiment': 1.0
        })
    )
