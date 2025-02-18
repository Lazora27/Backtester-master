import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DominantCycleOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DominantCycleOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DominantCycleOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
