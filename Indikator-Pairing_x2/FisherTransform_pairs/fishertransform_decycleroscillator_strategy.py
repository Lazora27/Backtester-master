import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
