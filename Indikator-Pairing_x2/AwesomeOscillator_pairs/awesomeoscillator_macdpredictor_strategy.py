import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'MACDPredictor': 1.0
        })
    )
