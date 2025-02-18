import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
