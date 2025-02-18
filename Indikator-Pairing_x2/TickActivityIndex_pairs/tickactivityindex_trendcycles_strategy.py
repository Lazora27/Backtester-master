import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
