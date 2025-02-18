import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'BuyingPressure': 1.0
        })
    )
