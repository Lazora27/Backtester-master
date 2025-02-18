import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
