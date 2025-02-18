import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und MassIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'MassIndex': 1.0
        })
    )
