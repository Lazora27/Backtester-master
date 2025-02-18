import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
