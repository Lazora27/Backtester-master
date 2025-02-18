import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'IntradayIntensity': 1.0
        })
    )
