import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
