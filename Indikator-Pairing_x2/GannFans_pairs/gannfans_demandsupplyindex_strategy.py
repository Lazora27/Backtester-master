import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
