import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
