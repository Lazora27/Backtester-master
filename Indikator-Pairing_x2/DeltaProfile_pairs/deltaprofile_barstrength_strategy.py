import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BarStrength
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BarStrength': 1.0
        })
    )
