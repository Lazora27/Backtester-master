import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'VolumeProfile': 1.0
        })
    )
