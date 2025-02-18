import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'KeltnerChannels': 1.0
        })
    )
