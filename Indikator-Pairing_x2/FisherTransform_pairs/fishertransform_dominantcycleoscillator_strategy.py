import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
