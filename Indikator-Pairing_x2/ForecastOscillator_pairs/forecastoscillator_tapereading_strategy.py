import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TapeReading
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TapeReading': 1.0
        })
    )
