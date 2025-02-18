import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'IntradayIntensity': 1.0
        })
    )
