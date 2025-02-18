import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandWidth_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandWidth und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BollingerBandWidth': 1.0,
            'IntradayIntensity': 1.0
        })
    )
