import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
