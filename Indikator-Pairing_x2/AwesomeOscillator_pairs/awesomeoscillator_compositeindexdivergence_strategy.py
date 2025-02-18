import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
