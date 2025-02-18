import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'DeltaProfile': 1.0
        })
    )
