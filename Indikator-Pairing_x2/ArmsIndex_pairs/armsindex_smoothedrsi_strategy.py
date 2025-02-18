import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
