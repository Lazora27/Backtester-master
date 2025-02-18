import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BuyingPressure': 1.0
        })
    )
