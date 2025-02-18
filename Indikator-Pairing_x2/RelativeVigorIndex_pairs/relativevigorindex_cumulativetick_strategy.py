import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
