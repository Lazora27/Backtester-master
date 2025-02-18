import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
