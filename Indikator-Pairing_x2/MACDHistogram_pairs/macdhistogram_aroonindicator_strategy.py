import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'AroonIndicator': 1.0
        })
    )
