import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'IntradayIntensity': 1.0
        })
    )
