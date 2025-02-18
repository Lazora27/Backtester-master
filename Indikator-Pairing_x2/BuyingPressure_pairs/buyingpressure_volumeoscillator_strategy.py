import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'VolumeOscillator': 1.0
        })
    )
