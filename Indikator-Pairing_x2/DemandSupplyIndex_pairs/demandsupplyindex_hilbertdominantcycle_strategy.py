import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
