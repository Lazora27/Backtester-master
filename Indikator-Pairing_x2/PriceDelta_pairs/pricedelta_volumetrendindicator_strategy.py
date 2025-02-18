import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
