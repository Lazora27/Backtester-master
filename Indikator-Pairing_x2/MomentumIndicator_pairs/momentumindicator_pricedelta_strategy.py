import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und PriceDelta
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'PriceDelta': 1.0
        })
    )
