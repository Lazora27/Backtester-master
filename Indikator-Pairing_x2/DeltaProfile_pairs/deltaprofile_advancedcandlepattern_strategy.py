import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
