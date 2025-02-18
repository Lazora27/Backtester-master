import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'IntradayIntensity': 1.0
        })
    )
