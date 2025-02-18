import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AverageLogRange': 1.0
        })
    )
