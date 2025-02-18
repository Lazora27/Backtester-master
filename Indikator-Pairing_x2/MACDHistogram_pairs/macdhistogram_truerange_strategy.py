import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und TrueRange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'TrueRange': 1.0
        })
    )
