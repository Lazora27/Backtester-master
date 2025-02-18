import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'TrendExhaustion': 1.0
        })
    )
