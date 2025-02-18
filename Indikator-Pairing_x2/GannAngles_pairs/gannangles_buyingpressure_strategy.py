import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'BuyingPressure': 1.0
        })
    )
