import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_LaggingVolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und LaggingVolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'LaggingVolatilityIndex': {
                'class': LaggingVolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LaggingVolatilityIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'LaggingVolatilityIndex': 1.0
        })
    )
