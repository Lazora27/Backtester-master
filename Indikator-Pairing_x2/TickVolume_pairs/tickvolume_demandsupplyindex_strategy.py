import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
