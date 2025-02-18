import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdaptiveRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdaptiveRSI
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdaptiveRSI': 1.0
        })
    )
