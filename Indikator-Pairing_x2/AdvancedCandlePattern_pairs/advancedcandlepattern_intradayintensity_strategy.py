import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'IntradayIntensity': 1.0
        })
    )
