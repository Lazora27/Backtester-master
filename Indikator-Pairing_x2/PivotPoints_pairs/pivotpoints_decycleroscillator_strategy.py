import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
