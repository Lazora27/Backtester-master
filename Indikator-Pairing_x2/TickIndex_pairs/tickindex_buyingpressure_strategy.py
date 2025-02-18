import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
