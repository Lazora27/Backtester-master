import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PutCallRatio': 1.0
        })
    )
