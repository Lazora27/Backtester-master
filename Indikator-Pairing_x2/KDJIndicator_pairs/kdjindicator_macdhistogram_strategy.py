import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MACDHistogram_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MACDHistogram
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MACDHistogram': 1.0
        })
    )
