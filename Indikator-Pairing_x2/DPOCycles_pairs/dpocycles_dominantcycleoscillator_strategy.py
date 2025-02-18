import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DPOCycles_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DPOCycles und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'DPOCycles': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
