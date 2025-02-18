import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'BuyingPressure': 1.0
        })
    )
