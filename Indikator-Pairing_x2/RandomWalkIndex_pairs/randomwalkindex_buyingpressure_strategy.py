import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
