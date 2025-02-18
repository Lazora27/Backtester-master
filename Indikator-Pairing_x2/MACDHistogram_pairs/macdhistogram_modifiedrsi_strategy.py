import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ModifiedRSI': 1.0
        })
    )
