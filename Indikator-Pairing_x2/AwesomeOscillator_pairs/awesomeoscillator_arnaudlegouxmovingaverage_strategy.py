import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ArnaudLegouxMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ArnaudLegouxMovingAverage
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ArnaudLegouxMovingAverage': {
                'class': ArnaudLegouxMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArnaudLegouxMovingAverage'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ArnaudLegouxMovingAverage': 1.0
        })
    )
