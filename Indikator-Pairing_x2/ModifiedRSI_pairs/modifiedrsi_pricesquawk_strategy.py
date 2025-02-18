import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PriceSquawk': 1.0
        })
    )
