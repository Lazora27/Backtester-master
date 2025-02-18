import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'IntradayIntensity': 1.0
        })
    )
