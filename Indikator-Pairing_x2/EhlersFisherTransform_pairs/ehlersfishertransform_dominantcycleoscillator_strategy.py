import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
