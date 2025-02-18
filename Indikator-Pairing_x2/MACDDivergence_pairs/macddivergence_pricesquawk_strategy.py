import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'PriceSquawk': 1.0
        })
    )
