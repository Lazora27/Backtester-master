import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
