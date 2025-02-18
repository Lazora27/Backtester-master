import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
