import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TrendCycles
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TrendCycles': 1.0
        })
    )
