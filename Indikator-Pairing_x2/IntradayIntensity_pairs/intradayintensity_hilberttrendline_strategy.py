import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'HilbertTrendline': 1.0
        })
    )
