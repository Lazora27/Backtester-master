import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
