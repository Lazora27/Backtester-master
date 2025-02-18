import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_KDJIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und KDJIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'KDJIndicator': 1.0
        })
    )
