import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'ForecastOscillator': 1.0
        })
    )
