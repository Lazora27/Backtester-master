import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AAIISentiment': 1.0
        })
    )
