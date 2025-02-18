import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
