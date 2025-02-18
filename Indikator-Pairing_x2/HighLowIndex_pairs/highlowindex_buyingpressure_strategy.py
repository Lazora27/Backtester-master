import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
