import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
