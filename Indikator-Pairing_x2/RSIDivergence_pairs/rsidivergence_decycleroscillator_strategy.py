import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
