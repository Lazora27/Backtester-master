import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'VolumeDelta': 1.0
        })
    )
