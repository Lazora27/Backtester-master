import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
