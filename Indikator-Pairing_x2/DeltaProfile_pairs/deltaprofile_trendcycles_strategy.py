import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und TrendCycles
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'TrendCycles': 1.0
        })
    )
