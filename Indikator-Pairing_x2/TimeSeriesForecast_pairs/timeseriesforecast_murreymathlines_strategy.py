import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'MurreyMathLines': 1.0
        })
    )
