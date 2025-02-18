import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'ForecastOscillator': 1.0
        })
    )
