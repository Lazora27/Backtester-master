import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und MassIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'MassIndex': 1.0
        })
    )
