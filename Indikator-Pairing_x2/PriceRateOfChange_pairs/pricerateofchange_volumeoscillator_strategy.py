import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'VolumeOscillator': 1.0
        })
    )
