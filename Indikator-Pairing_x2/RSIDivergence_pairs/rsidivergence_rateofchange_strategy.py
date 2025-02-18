import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und RateOfChange
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'RateOfChange': 1.0
        })
    )
