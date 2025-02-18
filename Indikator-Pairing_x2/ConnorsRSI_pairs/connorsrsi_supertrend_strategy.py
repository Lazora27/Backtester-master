import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'SuperTrend': 1.0
        })
    )
