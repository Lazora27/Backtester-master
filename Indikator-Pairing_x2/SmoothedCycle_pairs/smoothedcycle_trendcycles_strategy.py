import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedCycle_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedCycle und TrendCycles
    """
    
    params = (
        ('indicators', {
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'SmoothedCycle': 1.0,
            'TrendCycles': 1.0
        })
    )
