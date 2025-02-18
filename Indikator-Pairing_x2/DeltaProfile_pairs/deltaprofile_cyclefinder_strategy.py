import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und CycleFinder
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'CycleFinder': 1.0
        })
    )
