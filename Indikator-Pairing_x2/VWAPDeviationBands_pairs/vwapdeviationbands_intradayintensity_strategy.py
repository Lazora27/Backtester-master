import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'IntradayIntensity': 1.0
        })
    )
