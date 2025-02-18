import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
