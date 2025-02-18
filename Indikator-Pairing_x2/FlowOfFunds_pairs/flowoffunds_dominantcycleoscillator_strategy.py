import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
