import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'IntradayIntensity': 1.0
        })
    )
