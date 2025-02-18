import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
