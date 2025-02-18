import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und GannSquares
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'GannSquares': 1.0
        })
    )
