import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und GannFans
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'GannFans': 1.0
        })
    )
