import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
