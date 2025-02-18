import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
