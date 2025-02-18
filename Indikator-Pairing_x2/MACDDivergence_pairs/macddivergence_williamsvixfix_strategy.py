import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
