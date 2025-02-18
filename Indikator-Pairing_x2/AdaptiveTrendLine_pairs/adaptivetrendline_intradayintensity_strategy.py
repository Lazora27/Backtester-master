import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'IntradayIntensity': 1.0
        })
    )
