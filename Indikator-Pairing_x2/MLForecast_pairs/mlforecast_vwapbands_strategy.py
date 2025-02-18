import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VWAPBands': 1.0
        })
    )
