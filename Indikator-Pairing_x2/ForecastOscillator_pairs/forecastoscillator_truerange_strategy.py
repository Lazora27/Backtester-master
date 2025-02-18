import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TrueRange
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TrueRange': 1.0
        })
    )
