import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'BuyingPressure': 1.0
        })
    )
