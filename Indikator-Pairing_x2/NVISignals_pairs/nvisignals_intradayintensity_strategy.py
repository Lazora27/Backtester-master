import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'IntradayIntensity': 1.0
        })
    )
