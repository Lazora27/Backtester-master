import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SupplyDemandZones_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SupplyDemandZones und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'SupplyDemandZones': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
