import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_McClellanSummationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und McClellanSummationIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'McClellanSummationIndex': 1.0
        })
    )
