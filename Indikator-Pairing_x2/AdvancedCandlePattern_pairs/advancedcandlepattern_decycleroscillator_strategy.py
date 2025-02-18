import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
