import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VWAPBands
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VWAPBands': 1.0
        })
    )
