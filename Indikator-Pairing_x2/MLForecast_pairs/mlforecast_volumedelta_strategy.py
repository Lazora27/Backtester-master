import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VolumeDelta': 1.0
        })
    )
