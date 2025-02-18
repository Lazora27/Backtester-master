import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_PositiveVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und PositiveVolumeIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'PositiveVolumeIndex': 1.0
        })
    )
