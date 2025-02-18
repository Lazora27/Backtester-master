import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und FisherTransform
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'FisherTransform': 1.0
        })
    )
