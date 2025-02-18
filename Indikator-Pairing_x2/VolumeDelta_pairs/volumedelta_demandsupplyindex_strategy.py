import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
