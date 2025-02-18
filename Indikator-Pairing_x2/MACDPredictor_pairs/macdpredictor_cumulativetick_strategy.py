import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'CumulativeTick': 1.0
        })
    )
