import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArnaudLegouxMovingAverage_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArnaudLegouxMovingAverage und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ArnaudLegouxMovingAverage': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
