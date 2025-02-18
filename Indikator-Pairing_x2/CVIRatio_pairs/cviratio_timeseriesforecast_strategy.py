import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
