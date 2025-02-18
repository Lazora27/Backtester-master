import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
