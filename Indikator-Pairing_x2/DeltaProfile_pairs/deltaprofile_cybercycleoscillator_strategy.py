import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
