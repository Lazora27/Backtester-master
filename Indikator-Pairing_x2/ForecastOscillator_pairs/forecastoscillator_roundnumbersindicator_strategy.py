import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
