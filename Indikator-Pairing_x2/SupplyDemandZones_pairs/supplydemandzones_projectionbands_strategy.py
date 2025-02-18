import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'ProjectionBands': 1.0
        })
    )
