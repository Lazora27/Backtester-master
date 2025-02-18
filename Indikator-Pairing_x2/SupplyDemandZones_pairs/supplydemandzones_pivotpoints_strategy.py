import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und PivotPoints
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'PivotPoints': 1.0
        })
    )
