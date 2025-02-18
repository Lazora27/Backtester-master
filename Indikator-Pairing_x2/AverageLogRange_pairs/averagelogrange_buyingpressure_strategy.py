import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'BuyingPressure': 1.0
        })
    )
