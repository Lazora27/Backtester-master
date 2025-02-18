import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertPhaseIndicator_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertPhaseIndicator und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertPhaseIndicator': {
                'class': HilbertPhaseIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertPhaseIndicator'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HilbertPhaseIndicator': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
