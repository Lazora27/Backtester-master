import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'PhaseDivergence': 1.0
        })
    )
