import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
