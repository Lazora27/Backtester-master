import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
