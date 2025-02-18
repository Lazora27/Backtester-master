import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'IntradayIntensity': 1.0
        })
    )
