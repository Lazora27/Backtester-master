import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_TimeSeriesForecast_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und TimeSeriesForecast
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'TimeSeriesForecast': 1.0
        })
    )
