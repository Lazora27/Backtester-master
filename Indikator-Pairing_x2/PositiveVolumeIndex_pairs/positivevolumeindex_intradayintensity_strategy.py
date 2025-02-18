import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'IntradayIntensity': 1.0
        })
    )
