import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'GannSquareReversal': 1.0
        })
    )
