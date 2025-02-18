import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ZigZagIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ZigZagIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ZigZagIndicator': {
                'class': ZigZagIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ZigZagIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ZigZagIndicator': 1.0
        })
    )
