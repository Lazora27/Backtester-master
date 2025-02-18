import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
