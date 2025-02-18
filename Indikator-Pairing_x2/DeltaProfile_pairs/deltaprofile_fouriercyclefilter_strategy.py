import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
