import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'FearGreedIndex': 1.0
        })
    )
