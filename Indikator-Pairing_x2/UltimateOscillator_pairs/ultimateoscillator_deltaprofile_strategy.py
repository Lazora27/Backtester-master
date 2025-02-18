import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
