import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
