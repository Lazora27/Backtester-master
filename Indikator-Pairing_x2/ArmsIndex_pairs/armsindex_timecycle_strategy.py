import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
