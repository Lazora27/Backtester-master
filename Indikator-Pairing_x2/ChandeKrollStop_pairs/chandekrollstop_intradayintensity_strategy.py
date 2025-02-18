import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'IntradayIntensity': 1.0
        })
    )
