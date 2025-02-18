import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
