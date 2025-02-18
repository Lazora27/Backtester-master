import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und DOMDepth
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'DOMDepth': 1.0
        })
    )
