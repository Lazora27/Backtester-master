import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
