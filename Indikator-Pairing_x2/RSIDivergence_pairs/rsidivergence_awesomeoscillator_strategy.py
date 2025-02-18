import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_AwesomeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und AwesomeOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'AwesomeOscillator': 1.0
        })
    )
