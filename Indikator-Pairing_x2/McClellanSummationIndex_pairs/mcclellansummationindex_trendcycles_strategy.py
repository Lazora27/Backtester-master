import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und TrendCycles
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'TrendCycles': 1.0
        })
    )
