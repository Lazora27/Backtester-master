import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
