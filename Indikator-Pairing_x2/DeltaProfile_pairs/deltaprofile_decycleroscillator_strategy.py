import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
