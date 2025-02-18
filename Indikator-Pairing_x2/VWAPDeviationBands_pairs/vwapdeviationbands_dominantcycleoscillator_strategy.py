import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPDeviationBands_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPDeviationBands und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPDeviationBands': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
