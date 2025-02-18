import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
