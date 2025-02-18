import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
