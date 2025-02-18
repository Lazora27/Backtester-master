import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'CCITurbo': 1.0
        })
    )
