import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
