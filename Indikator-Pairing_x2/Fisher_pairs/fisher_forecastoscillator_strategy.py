import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'ForecastOscillator': 1.0
        })
    )
