import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
