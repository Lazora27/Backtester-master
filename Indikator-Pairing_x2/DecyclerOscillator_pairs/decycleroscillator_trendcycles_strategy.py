import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DecyclerOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DecyclerOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DecyclerOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
