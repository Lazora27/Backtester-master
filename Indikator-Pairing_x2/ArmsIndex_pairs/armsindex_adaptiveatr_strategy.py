import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
