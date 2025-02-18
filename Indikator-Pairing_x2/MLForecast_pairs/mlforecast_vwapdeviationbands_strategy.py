import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
