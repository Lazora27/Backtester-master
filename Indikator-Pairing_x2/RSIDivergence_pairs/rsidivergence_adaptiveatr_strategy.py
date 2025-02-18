import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AdaptiveATR': 1.0
        })
    )
