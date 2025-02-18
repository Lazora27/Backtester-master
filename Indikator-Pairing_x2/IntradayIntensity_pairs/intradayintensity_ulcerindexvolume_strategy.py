import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
