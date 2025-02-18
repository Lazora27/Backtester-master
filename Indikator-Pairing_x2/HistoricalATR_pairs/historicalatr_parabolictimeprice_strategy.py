import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
