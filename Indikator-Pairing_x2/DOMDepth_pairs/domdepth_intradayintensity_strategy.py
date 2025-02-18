import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'IntradayIntensity': 1.0
        })
    )
