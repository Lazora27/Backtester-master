import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
