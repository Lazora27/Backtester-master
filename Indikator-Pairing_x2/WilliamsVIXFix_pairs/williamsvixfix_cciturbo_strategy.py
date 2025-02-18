import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und CCITurbo
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'CCITurbo': 1.0
        })
    )
