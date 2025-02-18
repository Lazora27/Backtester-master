import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
