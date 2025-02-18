import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DemandSupplyIndex_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DemandSupplyIndex und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'DemandSupplyIndex': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
