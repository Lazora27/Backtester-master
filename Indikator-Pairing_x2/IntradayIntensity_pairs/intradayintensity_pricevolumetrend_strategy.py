import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
