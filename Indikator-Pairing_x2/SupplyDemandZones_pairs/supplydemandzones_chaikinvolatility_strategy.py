import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
