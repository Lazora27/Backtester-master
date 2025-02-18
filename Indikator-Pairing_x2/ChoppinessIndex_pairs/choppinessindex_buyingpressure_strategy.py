import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
