import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
