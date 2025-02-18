import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'WeightedCycle': 1.0
        })
    )
