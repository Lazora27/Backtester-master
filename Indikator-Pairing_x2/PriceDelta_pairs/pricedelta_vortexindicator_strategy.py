import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VortexIndicator': 1.0
        })
    )
