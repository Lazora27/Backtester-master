import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'IntradayIntensity': 1.0
        })
    )
