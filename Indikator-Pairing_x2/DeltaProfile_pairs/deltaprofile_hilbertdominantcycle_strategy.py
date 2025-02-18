import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
