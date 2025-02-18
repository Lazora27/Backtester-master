import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
