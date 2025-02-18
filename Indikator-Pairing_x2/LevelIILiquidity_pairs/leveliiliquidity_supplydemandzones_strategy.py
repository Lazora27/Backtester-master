import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LevelIILiquidity_SupplyDemandZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LevelIILiquidity und SupplyDemandZones
    """
    
    params = (
        ('indicators', {
            'LevelIILiquidity': {
                'class': LevelIILiquidity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LevelIILiquidity'>
            },
            'SupplyDemandZones': {
                'class': SupplyDemandZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SupplyDemandZones'>
            }
        }),
        ('weights', {
            'LevelIILiquidity': 1.0,
            'SupplyDemandZones': 1.0
        })
    )
