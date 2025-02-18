import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und TrendCycles
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'TrendCycles': 1.0
        })
    )
