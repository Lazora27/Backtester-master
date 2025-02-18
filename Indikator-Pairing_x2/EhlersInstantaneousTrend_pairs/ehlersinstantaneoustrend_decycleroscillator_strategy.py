import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrend_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrend und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrend': {
                'class': EhlersInstantaneousTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrend'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrend': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
