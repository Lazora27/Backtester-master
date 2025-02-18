import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und SuperMACD
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'SuperMACD': 1.0
        })
    )
