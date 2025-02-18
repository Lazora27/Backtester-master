import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
