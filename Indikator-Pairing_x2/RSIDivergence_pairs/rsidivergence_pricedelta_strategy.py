import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PriceDelta
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PriceDelta': 1.0
        })
    )
