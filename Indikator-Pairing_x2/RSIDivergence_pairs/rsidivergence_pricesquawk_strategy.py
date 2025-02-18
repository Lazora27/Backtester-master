import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PriceSquawk': 1.0
        })
    )
