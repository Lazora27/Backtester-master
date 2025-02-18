import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'TRIXIndicator': 1.0
        })
    )
