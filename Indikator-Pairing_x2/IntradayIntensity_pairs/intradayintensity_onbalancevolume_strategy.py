import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
