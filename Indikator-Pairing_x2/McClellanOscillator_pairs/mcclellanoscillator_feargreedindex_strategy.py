import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'FearGreedIndex': 1.0
        })
    )
