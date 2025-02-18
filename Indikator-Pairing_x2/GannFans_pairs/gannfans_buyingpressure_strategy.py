import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'BuyingPressure': 1.0
        })
    )
