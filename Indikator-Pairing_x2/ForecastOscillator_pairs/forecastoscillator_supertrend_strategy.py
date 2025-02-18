import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'SuperTrend': 1.0
        })
    )
