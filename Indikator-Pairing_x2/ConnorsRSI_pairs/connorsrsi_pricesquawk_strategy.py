import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'PriceSquawk': 1.0
        })
    )
