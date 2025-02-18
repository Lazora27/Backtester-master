import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeCycle_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeCycle und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TimeCycle': 1.0,
            'TrendCycles': 1.0
        })
    )
