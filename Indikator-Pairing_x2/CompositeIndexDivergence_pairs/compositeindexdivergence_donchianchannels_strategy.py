import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'DonchianChannels': 1.0
        })
    )
