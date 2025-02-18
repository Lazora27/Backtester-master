import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
