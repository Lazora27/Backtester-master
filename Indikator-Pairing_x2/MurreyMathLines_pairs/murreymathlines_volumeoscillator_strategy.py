import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VolumeOscillator': 1.0
        })
    )
