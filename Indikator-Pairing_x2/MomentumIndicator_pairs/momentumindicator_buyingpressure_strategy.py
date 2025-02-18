import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'BuyingPressure': 1.0
        })
    )
