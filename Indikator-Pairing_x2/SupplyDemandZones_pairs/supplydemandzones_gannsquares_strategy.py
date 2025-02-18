import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und GannSquares
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'GannSquares': 1.0
        })
    )
