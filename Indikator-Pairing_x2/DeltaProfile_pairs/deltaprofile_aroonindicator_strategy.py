import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AroonIndicator': 1.0
        })
    )
