import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_EldersForceIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und EldersForceIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'EldersForceIndex': 1.0
        })
    )
