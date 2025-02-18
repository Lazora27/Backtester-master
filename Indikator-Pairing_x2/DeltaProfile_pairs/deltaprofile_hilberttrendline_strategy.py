import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HilbertTrendline': 1.0
        })
    )
