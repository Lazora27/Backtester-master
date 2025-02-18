import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
