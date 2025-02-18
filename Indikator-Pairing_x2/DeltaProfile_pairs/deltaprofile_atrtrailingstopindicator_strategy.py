import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ATRTrailingStopIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ATRTrailingStopIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ATRTrailingStopIndicator': {
                'class': ATRTrailingStopIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ATRTrailingStopIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ATRTrailingStopIndicator': 1.0
        })
    )
