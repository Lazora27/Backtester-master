import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
