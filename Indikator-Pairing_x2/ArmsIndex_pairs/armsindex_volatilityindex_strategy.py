import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VolatilityIndex': 1.0
        })
    )
