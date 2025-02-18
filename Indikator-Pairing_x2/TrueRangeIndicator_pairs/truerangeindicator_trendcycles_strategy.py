import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRangeIndicator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRangeIndicator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TrueRangeIndicator': 1.0,
            'TrendCycles': 1.0
        })
    )
