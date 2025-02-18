import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
