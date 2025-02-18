import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolumeOscillator': 1.0
        })
    )
