import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
