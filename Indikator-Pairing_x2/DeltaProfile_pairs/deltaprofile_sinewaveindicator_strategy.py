import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
