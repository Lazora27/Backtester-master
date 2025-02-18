import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FearGreedIndex': 1.0
        })
    )
