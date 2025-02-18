import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
