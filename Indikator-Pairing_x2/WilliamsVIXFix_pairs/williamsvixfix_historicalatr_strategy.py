import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_HistoricalATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und HistoricalATR
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'HistoricalATR': 1.0
        })
    )
