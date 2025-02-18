import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
