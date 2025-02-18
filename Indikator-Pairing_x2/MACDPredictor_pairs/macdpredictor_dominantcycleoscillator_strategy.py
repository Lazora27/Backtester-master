import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
