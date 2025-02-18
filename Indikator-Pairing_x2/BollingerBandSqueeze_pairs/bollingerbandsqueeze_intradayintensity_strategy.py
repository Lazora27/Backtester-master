import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'IntradayIntensity': 1.0
        })
    )
