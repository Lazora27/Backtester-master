import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
