import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExtensionProjections_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExtensionProjections und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ExtensionProjections': 1.0,
            'BuyingPressure': 1.0
        })
    )
