import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'CumulativeTick': 1.0
        })
    )
