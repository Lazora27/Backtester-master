import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BuyingPressure': 1.0
        })
    )
