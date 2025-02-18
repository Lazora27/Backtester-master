import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
