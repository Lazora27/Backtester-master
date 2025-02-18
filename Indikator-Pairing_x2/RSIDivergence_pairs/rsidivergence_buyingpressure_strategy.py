import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'BuyingPressure': 1.0
        })
    )
