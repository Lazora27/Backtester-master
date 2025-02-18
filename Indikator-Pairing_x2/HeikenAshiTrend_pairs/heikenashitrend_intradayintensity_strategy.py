import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiTrend_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiTrend und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HeikenAshiTrend': 1.0,
            'IntradayIntensity': 1.0
        })
    )
