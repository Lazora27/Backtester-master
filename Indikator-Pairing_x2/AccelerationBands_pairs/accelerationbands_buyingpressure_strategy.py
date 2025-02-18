import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'BuyingPressure': 1.0
        })
    )
