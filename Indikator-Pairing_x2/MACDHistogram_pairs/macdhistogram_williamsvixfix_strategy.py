import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
