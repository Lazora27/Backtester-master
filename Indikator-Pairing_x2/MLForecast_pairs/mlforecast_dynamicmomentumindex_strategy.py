import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DynamicMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DynamicMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DynamicMomentumIndex': 1.0
        })
    )
