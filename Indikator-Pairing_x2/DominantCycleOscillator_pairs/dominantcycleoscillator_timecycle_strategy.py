import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DominantCycleOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DominantCycleOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DominantCycleOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
