import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
