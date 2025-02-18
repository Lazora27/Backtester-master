import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und BollingerBands
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'BollingerBands': 1.0
        })
    )
