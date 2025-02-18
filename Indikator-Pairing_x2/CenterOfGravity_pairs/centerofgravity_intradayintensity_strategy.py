import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'IntradayIntensity': 1.0
        })
    )
