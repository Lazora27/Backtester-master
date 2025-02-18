import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertTrendSignals_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertTrendSignals und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'HilbertTrendSignals': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
