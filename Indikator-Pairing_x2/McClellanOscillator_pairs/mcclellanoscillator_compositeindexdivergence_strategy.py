import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
