import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MarketCycleIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MarketCycleIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MarketCycleIndicator': {
                'class': MarketCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketCycleIndicator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MarketCycleIndicator': 1.0
        })
    )
