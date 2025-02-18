import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
