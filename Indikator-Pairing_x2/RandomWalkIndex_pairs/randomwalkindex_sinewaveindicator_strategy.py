import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
