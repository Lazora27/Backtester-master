import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
