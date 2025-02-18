import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
