import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TrueRange
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TrueRange': 1.0
        })
    )
