import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'KeltnerChannels': 1.0
        })
    )
