import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
