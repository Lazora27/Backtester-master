import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'AdaptiveATR': 1.0
        })
    )
