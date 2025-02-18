import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'BuyingPressure': 1.0
        })
    )
