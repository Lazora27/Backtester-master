import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
