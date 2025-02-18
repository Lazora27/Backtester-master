import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BuyingPressure': 1.0
        })
    )
