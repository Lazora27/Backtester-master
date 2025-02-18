import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
