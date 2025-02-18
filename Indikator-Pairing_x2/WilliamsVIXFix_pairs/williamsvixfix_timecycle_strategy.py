import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TimeCycle
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TimeCycle': 1.0
        })
    )
