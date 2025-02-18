import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'IntradayIntensity': 1.0
        })
    )
