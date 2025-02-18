import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
