import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ForecastOscillator': 1.0
        })
    )
