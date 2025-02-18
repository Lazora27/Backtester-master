import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'BuyingPressure': 1.0
        })
    )
