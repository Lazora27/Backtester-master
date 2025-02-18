import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'AccelerationBands': 1.0
        })
    )
