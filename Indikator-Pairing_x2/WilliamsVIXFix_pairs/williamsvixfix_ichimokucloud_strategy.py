import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'IchimokuCloud': 1.0
        })
    )
