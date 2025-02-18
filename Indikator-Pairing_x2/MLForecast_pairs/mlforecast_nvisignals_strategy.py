import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_NVISignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und NVISignals
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'NVISignals': 1.0
        })
    )
