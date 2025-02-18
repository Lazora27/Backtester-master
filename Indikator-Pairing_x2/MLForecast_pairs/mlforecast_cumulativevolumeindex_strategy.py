import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_CumulativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und CumulativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'CumulativeVolumeIndex': {
                'class': CumulativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeVolumeIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'CumulativeVolumeIndex': 1.0
        })
    )
