import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TrendCycles': 1.0
        })
    )
