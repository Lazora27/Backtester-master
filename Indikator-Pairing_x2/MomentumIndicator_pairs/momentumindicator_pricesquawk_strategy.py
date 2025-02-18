import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PriceSquawk': 1.0
        })
    )
