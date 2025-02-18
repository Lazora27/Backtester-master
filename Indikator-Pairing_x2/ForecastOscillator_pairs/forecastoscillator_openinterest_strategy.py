import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'OpenInterest': 1.0
        })
    )
