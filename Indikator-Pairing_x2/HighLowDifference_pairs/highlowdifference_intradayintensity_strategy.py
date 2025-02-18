import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'IntradayIntensity': 1.0
        })
    )
