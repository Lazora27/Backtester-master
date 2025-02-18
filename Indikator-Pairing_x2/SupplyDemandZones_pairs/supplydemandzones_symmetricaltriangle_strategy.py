import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
