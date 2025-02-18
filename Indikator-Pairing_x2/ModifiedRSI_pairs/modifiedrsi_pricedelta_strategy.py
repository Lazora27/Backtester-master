import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und PriceDelta
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'PriceDelta': 1.0
        })
    )
