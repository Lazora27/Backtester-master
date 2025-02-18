import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
