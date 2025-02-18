import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
