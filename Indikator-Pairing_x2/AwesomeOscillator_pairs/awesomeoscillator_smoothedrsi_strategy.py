import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'SmoothedRSI': 1.0
        })
    )
