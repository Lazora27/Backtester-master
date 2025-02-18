import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
