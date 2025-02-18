import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PVINVIComparison_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PVINVIComparison
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PVINVIComparison': 1.0
        })
    )
