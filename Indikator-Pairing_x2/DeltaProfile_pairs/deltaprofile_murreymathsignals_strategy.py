import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
