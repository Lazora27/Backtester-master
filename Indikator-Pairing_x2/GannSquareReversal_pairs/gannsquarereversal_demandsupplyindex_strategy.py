import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
