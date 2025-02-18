import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'UlcerIndex': 1.0
        })
    )
