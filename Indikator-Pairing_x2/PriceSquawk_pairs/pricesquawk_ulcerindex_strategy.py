import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'UlcerIndex': 1.0
        })
    )
