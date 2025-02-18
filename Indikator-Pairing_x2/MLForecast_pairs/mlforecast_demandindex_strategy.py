import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DemandIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DemandIndex': 1.0
        })
    )
