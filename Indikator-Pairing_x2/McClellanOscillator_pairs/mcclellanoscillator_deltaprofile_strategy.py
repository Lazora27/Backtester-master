import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'DeltaProfile': 1.0
        })
    )
