import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'IntradayIntensity': 1.0
        })
    )
