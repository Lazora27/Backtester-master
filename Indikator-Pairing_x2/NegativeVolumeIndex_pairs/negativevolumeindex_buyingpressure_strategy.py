import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
