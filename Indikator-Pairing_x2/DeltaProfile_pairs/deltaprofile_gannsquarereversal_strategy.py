import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'GannSquareReversal': 1.0
        })
    )
