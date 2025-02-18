import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IntradayIntensity_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IntradayIntensity und CyberCycle
    """
    
    params = (
        ('indicators', {
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'IntradayIntensity': 1.0,
            'CyberCycle': 1.0
        })
    )
