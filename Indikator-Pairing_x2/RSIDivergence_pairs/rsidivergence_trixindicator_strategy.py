import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'TRIXIndicator': 1.0
        })
    )
