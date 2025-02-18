import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TickActivityIndex': 1.0
        })
    )
