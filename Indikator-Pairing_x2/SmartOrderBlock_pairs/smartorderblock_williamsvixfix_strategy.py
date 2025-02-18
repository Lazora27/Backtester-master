import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
