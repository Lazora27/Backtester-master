import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
