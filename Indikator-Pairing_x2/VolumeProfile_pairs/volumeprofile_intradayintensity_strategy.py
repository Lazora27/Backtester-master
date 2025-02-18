import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'IntradayIntensity': 1.0
        })
    )
