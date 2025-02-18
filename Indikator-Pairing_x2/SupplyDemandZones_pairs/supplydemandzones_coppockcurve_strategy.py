import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'CoppockCurve': 1.0
        })
    )
