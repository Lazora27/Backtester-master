import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
