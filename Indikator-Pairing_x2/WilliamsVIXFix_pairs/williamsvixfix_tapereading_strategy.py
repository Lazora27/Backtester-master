import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TapeReading_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TapeReading
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TapeReading': 1.0
        })
    )
