import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSeriesForecast_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSeriesForecast und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'TimeSeriesForecast': {
                'class': TimeSeriesForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSeriesForecast'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'TimeSeriesForecast': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
