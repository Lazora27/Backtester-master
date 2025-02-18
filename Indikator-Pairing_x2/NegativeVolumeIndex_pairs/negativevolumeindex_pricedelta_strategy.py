import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
