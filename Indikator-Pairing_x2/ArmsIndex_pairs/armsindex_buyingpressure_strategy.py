import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
