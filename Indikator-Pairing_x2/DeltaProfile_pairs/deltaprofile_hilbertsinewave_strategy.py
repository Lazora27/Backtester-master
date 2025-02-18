import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HilbertSinewave': 1.0
        })
    )
